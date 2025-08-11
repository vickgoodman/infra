# beman-tidy: The Codebase Bemanification Tool

<!--
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
-->

## Description

`beman-tidy` is a tool used to check and apply
[The Beman Standard](https://github.com/bemanproject/beman/blob/main/docs/beman_standard.md).

Purpose: The tool is used to `check` (`--dry-run`) and `apply` (`--fix-inplace`) the Beman Standard to a repository.
Note: `2025-06-07`: In order to make the best and quickly use of the tool in the entire organization, most of the
checks will not support the `--fix-inplace` flag in the first iteration.

## Installation

- The current recommended workflow relies on [Astral's uv](https://docs.astral.sh/uv/)
- However, we provide a [PEP 751](https://peps.python.org/pep-0751/) `pylock.toml`, so don't feel forced to use uv
- You can use beman-tidy as a pre-commit hook or install it on your system using `pipx`

```shell
uv build
pipx install path/to/wheel
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

- Display help:

```shell
$ uv run beman-tidy --help
usage: beman-tidy [-h] [--fix-inplace | --no-fix-inplace] [--verbose | --no-verbose] [--require-all | --no-require-all] [--checks CHECKS] repo_path

positional arguments:
  repo_path             path to the repository to check

options:
  -h, --help            show this help message and exit
  --fix-inplace, --no-fix-inplace
                        Try to automatically fix found issues
  --verbose, --no-verbose
                        print verbose output for each check
  --require-all, --no-require-all
                        all checks are required regardless of the check type (e.g., Recommendation becomes Requirement)
  --checks CHECKS       array of checks to run
```

- Run beman-tidy on the exemplar repository **(default: dry-run mode)**

```shell
# dry-run, require-all, non-verbose
$ uv run beman-tidy /path/to/exemplar --require-all
Summary    Requirement:  18 checks passed, 1 checks failed, 5 checks skipped,  23 checks not implemented.
Summary Recommendation:  0 checks passed, 0 checks failed, 0 checks skipped,  0 checks not implemented.

Coverage    Requirement:  95.83% (23/24 checks passed).
Coverage Recommendation:   0.00% (0/0 checks passed).
Coverage          TOTAL:  95.83% (23/24 checks passed).

# dry-run, non-require-all, non-verbose
Summary    Requirement:  13 checks passed, 1 checks failed, 3 checks skipped,  9 checks not implemented.
Summary Recommendation:  5 checks passed, 0 checks failed, 2 checks skipped,  14 checks not implemented.

Coverage    Requirement:  66.67% (16/24 checks passed).
Coverage Recommendation: 100.00% (7/7 checks passed).
Coverage          TOTAL:  74.19% (23/31 checks passed).
```

or verbose mode:

```shell
# dry-run, require-all, verbose mode - no errors
$ uv run beman-tidy /path/to/exemplar --require-all --verbose
beman-tidy pipeline started ...

Running check [Recommendation][readme.title] ...
    check [Recommendation][readme.title] ... passed

Running check [Requirement][readme.badges] ...
    check [Requirement][readme.badges] ... passed

Running check [Recommendation][readme.library_status] ...
    check [Recommendation][readme.library_status] ... passed

Running check [Recommendation][directory.sources] ...
[warning        ][directory.sources        ]: The directory '/Users/dariusn/dev/dn/git/Beman/exemplar/src/beman/exemplar' does not exist.
check [Recommendation][directory.sources] ... failed


beman-tidy pipeline finished.

Summary    Requirement:  1 checks passed, 0 checks failed, 4 skipped (not implemented).
Summary Recommendation:  2 checks passed, 1 checks failed, 35 skipped (not implemented).

Coverage    Requirement: 100.0% (1/1 checks passed).
Coverage Recommendation: 66.67% (2/3 checks passed).
```

```shell
# dry-run, require-all, verbose mode - with errors
$ uv run beman-tidy /path/to/exemplar --require-all --verbose
beman-tidy pipeline started ...

Running check [Recommendation][readme.title] ...
    check [Recommendation][readme.title] ... passed

Running check [Requirement][readme.badges] ...
    check [Requirement][readme.badges] ... passed

Running check [Recommendation][readme.library_status] ...
    check [Recommendation][readme.library_status] ... passed

Running check [Recommendation][directory.sources] ...
check [Recommendation][directory.sources] ... passed


beman-tidy pipeline finished.

Summary    Requirement:  1 checks passed, 0 checks failed, 4 skipped (not implemented).
Summary Recommendation:  3 checks passed, 0 checks failed, 35 skipped (not implemented).

Coverage    Requirement: 100.0% (1/1 checks passed).
Coverage Recommendation: 100.0% (3/3 checks passed).
```

- Run beman-tidy on the exemplar repository (fix issues in-place):

```shell
uv run beman-tidy path/to/exemplar --fix-inplace --verbose
```

## beman-tidy Development

Please refer to the [Beman Tidy Development Guide](./docs/dev-guide.md) for more details.
