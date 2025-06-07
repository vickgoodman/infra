# beman-tidy: The Codebase Bemanification Tool

<!--
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
-->

## Description

`beman-tidy` is a tool used to check and apply [The Beman Standard](https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md).

Purpose: The tool is used to `check` (`--dry-run`) and `apply` (`--fix-inplace`) the Beman Standard to a repository.

Expected Development Flow:

* Find a Beman Standard check that is not implemented.
* Add a new entry to the `.beman-standard.yml` file.
* Add a new check to the `lib/checks/beman_standard/` directory (find existing checks for inspiration).
* Add tests for the new check.
* Run the tests.

Notes:
* `07.06.2025`: In order to make the best and quickly use of the tool in the entire organization, most of the checks will not support the `--fix-inplace` flag in the first iteration.
* `07.06.2025`: The Beman Standard is not stable right now, as the tool is still in development and the organization is still in the process of creating the standard. At some point, the standard will be stable. Until then, there may be a loop where implementing a check into the tool may also generates small changes to the standard (e.g., for automated fixes).

## Installation

```shell
$ make install
# or
$ pip3 install -r requirements.txt
```

## Usage

* Display help:
```shell
$ ./beman-tidy --help
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

* Run beman-tidy on the exemplar repository (default: dry-run mode)

```shell
$ ./beman-tidy ../exemplar --verbose
beman-tidy started ...

Running check [REQUIREMENT][TOPLEVEL.CHANGELOG] ...
    check [REQUIREMENT][TOPLEVEL.CHANGELOG] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.CMAKE] ...
    check [REQUIREMENT][TOPLEVEL.CMAKE] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.LICENSE] ...
    check [REQUIREMENT][TOPLEVEL.LICENSE] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.README] ...
    check [REQUIREMENT][TOPLEVEL.README] ... PASSED

Running check [REQUIREMENT][CHANGELOG.TITLE] ...
    check [REQUIREMENT][CHANGELOG.TITLE] ... PASSED

Running check [REQUIREMENT][CHANGELOG.LIBRARY_STATUS] ...
    check [REQUIREMENT][CHANGELOG.LIBRARY_STATUS] ... PASSED

Running check [RECOMMENDATION][README.TITLE] ...
    check [RECOMMENDATION][README.TITLE] ... FAILED

Running check [REQUIREMENT][README.BADGES] ...
[ERROR          ][README.BADGES            ]: Only one line of badges is allowed.
[ERROR          ][README.BADGES            ]: First line of README.md must contain badges.
    check [REQUIREMENT][README.BADGES] ... FAILED

Running check [RECOMMENDATION][README.IMPLEMENTS] ...
    check [RECOMMENDATION][README.IMPLEMENTS] ... PASSED

Running check [REQUIREMENT][README.LIBRARY_STATUS] ...
    check [REQUIREMENT][README.LIBRARY_STATUS] ... PASSED


beman-tidy finished.

Summary: 8 checks PASSED, 2 checks FAILED, 35 skipped (not implemented).

Coverage: 17.78% (8/45 checks passed).
```

* Run beman-tidy on the exemplar repository (fix issues in-place):

```shell
$ ./beman-tidy ../exemplar --fix-inplace --verbose
```

## Development

### Tree structure

```shell
 $ tree .
.
├── beman-tidy                             # The beman-tidy tool entry point (Python script).
├── .beman-standard.yml                    # The Beman Standard configuration file.
├── __init__.py                            # Allows recursive Python packages imports.
├── README.md                              # Root README / docs.
├── Makefile                               # Makefile for the beman-tidy tool.
├── requirements.txt                       # Production requirements.
├── requirements-dev.txt                   # Development requirements.
├── lib                                    # The library for the beman-tidy tool (e.g, checks, utils, etc.).
│   ├── __init__.py                        # Recursive Python packages imports
│   ├── checks                             # The checks for the beman-tidy tool.
│   │   ├── __init__.py
│   │   ├── base                           # Base classes for the checks - not to be used directly.
│   │   │   ├── __init__.py
│   │   │   ├── base_check.py              # Base class for all checks.
│   │   │   ├── directory_base_check.py    # Base class for directory checks.
│   │   │   └── file_base_check.py         # Base class for file checks.
│   │   ├── beman_standard                 # The ACTUAL checks for the beman standard.
│   │   │   ├── __init__.py
│   │   │   ├── cmake.py                   # CMake related checks.
│   │   │   ├── cpp.py                     # C++ related checks.
│   │   │   ├── directory.py               # Directory related checks.
│   │   │   ├── file.py                    # File related checks.
│   │   │   ├── general.py                 # General checks.
│   │   │   ├── license.py                 # License related checks.
│   │   │   ├── readme.py                  # README.md related checks.
│   │   │   ├── release.py                 # Release related checks.
│   │   │   └── toplevel.py                # Top-level checks.
│   │   └── system                         # System related checks.
│   │       ├── __init__.py
│   │       ├── git.py                     # Git related checks (internal use only).
│   │       └── registry.py                # Registry related checks (internal use only).
│   ├── pipeline.py                        # The pipeline for the beman-tidy tool.
│   └── utils                              # Utility functions for the beman-tidy tool.
│       ├── __init__.py
│       ├── git.py
│       ├── string.py
│       └── terminal.py
└── tests                                  # The tests for the beman-tidy tool.
    ├── __init__.py
    ├── beman_standard
    │   ├── __init__.py
    │   └── readme                         # The tests for the README.md check.
    │       ├── __init__.py
    │       ├── conftest.py                # The conftest for the pytest tests.
    │       ├── data                       # The data for the tests (e.g., file, directory, etc.).
    │       │   ├── invalid
    │       │   │   ├── README.md
    │       │   │   └── README.md.delete_me
    │       │   └── valid
    │       │       └── README.md
    │       └── test_readme.py
    ├── conftest.py
    └── utils
        ├── __init__.py
        └── conftest.py

24 directories, 62 files
```

Notes:

* `beman-tidy`: A Python script that is used to check and apply the Beman Standard to a repository.
* `.beman-standard.yml`: Stable version of the standard; the tool does not fetch the latest unstable version of the standard.
* `lib/`: The library for the beman-tidy tool (e.g, checks, utils, etc.).
   * `lib/checks/beman_standard/`: Direct implementation of the checks from the standard (e.g, `lib/checks/beman_standard/readme.py` is the implementation of the `README.md` checks).
   * `lib/checks/base/`: Base classes for the checks - not to be used directly.
   * `lib/pipeline.py`: The pipeline for the `beman-tidy` tool.
* `tests/`: The tests for the beman-tidy tool.
   * Structure is similar to the `lib/` directory.
   * `pytest` is used for testing.

### Linting

Run the linter:

```shell
# Run the linter - dry run.
$ make lint
# Run the linter - fix issues.
$ make lint-fix
```

### Running Tests

Run the tests:

```shell
$ make install-dev
pip3 install -r requirements-dev.txt
...q
$ make test
python3 -m pytest tests/ -v
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.9.6, pytest-8.4.0, pluggy-1.6.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/dariusn/dev/dn/git/Beman/infra/tools/beman-tidy
collected 3 items

tests/beman_standard/readme/test_readme.py::test_valid_readme_title PASSED                                                                                                                                                      [ 33%]
tests/beman_standard/readme/test_readme.py::test_invalid_readme_title PASSED                                                                                                                                                    [ 66%]
tests/beman_standard/readme/test_readme.py::test_fix_invalid_readme_title PASSED                                                                                                                                                [100%]

========================================================================================================== 3 passed in 0.08s ==========================================================================================================

```
