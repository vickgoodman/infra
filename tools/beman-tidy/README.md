# beman-tidy: The Codebase Bemanification Tool

<!--
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
-->

## Description

`beman-tidy` is a tool used to check and apply [The Beman Standard](https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md).

Purpose: The tool is used to `check` (`--dry-run`) and `apply` (`--fix-inplace`) the Beman Standard to a repository.
Note: `2025-06-07`: In order to make the best and quickly use of the tool in the entire organization, most of the checks will not support the `--fix-inplace` flag in the first iteration.

## Installation

- The current recommended workflow relies on [Astral's uv](https://docs.astral.sh/uv/)
- However, we provide a [PEP 751](https://peps.python.org/pep-0751/) `pylock.toml`, so don't feel forced to use uv
- You can use beman-tidy as a pre-commit hook or install it on your system using `pipx`

```shell
$ uv build
$ pipx install path/to/wheel
```

<details>
<summary>beman-tidy: Full example - build and install</summary>

```shell
$ uv build
Building source distribution...
Building wheel from source distribution...
Successfully built dist/beman_tidy-0.1.0.tar.gz
Successfully built dist/beman_tidy-0.1.0-py3-none-any.whl

$ pipx install dist/beman_tidy-0.1.0-py3-none-any.whl
Installing to existing venv 'beman-tidy'
  installed package beman-tidy 0.1.0, installed using Python 3.13.4
  These apps are now globally available
    - beman-tidy
...
You will need to open a new terminal or re-login for the PATH changes to take effect. Alternatively, you can source your shell's config file with e.g. 'source ~/.bashrc'.

$ beman-tidy --help
usage: beman-tidy [-h] [--fix-inplace | --no-fix-inplace] [--verbose | --no-verbose] [--checks CHECKS] repo_path
...
```

</details>

## Usage

* Display help:

```shell
$ uv run beman-tidy --help
usage: beman-tidy [-h] [--fix-inplace | --no-fix-inplace] [--verbose | --no-verbose] [--checks CHECKS] repo_path

positional arguments:
  repo_path             path to the repository to check

optional arguments:
  -h, --help            show this help message and exit
  --fix-inplace, --no-fix-inplace
                        Try to automatically fix found issues (default: False)
  --verbose, --no-verbose
                        print verbose output for each check (default: False)
  --checks CHECKS       array of checks to run
```

* Run beman-tidy on the exemplar repository **(default: dry-run mode)**

```shell
$ uv run beman-tidy path/to/exemplar
# non-verbose mode
Summary:  2 checks PASSED, 1 checks FAILED, 40 skipped (NOT implemented).

Coverage: 66.67% (2/3 checks passed).

# verbose mode - no errors
$ uv run beman-tidy /path/to/exemplar --verbose
beman-tidy pipeline started ...

  Running check [RECOMMENDATION][README.TITLE] ...
  [WARNING        ][README.TITLE             ]: The first line of the file '/Users/dariusn/dev/dn/git/Beman/exemplar/README.md' is invalid. It should start with '# beman.exemplar: <short_description>'.
    check [RECOMMENDATION][README.TITLE] ... FAILED

  Running check [RECOMMENDATION][README.BADGES] ...
    check [RECOMMENDATION][README.BADGES] ... PASSED

  Running check [RECOMMENDATION][README.LIBRARY_STATUS] ...
    check [RECOMMENDATION][README.LIBRARY_STATUS] ... PASSED


  beman-tidy pipeline finished.

  Summary:  2 checks PASSED, 1 checks FAILED, 40 skipped (NOT implemented).

Coverage: 66.67% (2/3 checks passed).
```

- Run beman-tidy in verbose mode

```shell
$ uv run /path/to/exemplar --verbose
beman-tidy pipeline started ...

Running check [RECOMMENDATION][README.TITLE] ...
  check [RECOMMENDATION][README.TITLE] ... PASSED

Running check [RECOMMENDATION][README.BADGES] ...
  check [RECOMMENDATION][README.BADGES] ... PASSED

Running check [RECOMMENDATION][README.LIBRARY_STATUS] ...
  check [RECOMMENDATION][README.LIBRARY_STATUS] ... PASSED


beman-tidy pipeline finished.

Summary:  3 checks PASSED, 0 checks FAILED, 40 skipped (NOT implemented).

Coverage: 100.0% (3/3 checks passed).
```

* Run beman-tidy on the exemplar repository (fix issues in-place):

```shell
$ uv run beman-tidy path/to/exemplar --fix-inplace --verbose
```

## beman-tidy Development

Please refer to the [Beman Tidy Development Guide](./docs/dev-guide.md) for more details.
