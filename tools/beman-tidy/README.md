# beman-tidy: Codebase Beminification Tool

<!--
SPDX-License-Identifier: 2.0 license with LLVM exceptions
-->

## Description

TODO: Add a description.

`beman-tidy` is a tool used to check and apply [The Beman Standard](https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md).

## Installation

TODO: Add an installation section.

## Usage

```shell
$ ./tools/beman-tidy/beman-tidy --help
usage: beman-tidy [-h] --repo-path REPO_PATH [--fix-inplace | --no-fix-inplace] [--verbose | --no-verbose]

optional arguments:
  -h, --help            show this help message and exit
  --repo-path REPO_PATH
                        path to the repository to check
  --fix-inplace, --no-fix-inplace
                        try to automatically fix found issues (default: False)
  --verbose, --no-verbose
                        print verbose output for each check (default: False)
```

More examples:

```shell
# Run checks and DO NOT fix issues and DO NOT print verbose output.
$ ./tools/beman-tidy/beman-tidy --repo-path ../exemplar
beman-tidy coverage: 11.11% (5/45 checks passed).

# Run checks and DO NOT fix issues and print verbose output.
$ ./tools/beman-tidy/beman-tidy --repo-path ../exemplar --verbose
beman-tidy started ...

Running check [REQUIREMENT][NO_UNSTAGED_CHANGES] ...
	check [REQUIREMENT][NO_UNSTAGED_CHANGES] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.CHANGELOG] ...
[ERROR          ][TOPLEVEL.CHANGELOG       ]: The file '/Users/dariusn/dev/dn/git/Beman/exemplar/CHANGELOG.md' does not exist.
	check [REQUIREMENT][TOPLEVEL.CHANGELOG] ... FAILED

Running check [REQUIREMENT][TOPLEVEL.CMAKE] ...
	check [REQUIREMENT][TOPLEVEL.CMAKE] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.LICENSE] ...
	check [REQUIREMENT][TOPLEVEL.LICENSE] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.README] ...
	check [REQUIREMENT][TOPLEVEL.README] ... PASSED

Running check [REQUIREMENT][CHANGELOG.TITLE] ...
[ERROR          ][CHANGELOG.TITLE          ]: The file '/Users/dariusn/dev/dn/git/Beman/exemplar/Changelog.md' does not exist.
	check [REQUIREMENT][CHANGELOG.TITLE] ... FAILED

Running check [REQUIREMENT][CHANGELOG.LIBRARY_STATUS] ...
[ERROR          ][CHANGELOG.LIBRARY_STATUS ]: The file '/Users/dariusn/dev/dn/git/Beman/exemplar/Changelog.md' does not exist.
	check [REQUIREMENT][CHANGELOG.LIBRARY_STATUS] ... FAILED

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


beman-tidy coverage: 11.11% (5/45 checks passed).

# Run checks and fix issues and print verbose output.
$ ./tools/beman-tidy/beman-tidy --repo-path ../exemplar --verbose --fix-inplace
beman-tidy started ...

Running check [REQUIREMENT][NO_UNSTAGED_CHANGES] ...
	check [REQUIREMENT][NO_UNSTAGED_CHANGES] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.CHANGELOG] ...
[ERROR          ][TOPLEVEL.CHANGELOG       ]: The file '/Users/dariusn/dev/dn/git/Beman/exemplar/CHANGELOG.md' does not exist.
	check [REQUIREMENT][TOPLEVEL.CHANGELOG] ... FAILED

Running check [REQUIREMENT][TOPLEVEL.CMAKE] ...
	check [REQUIREMENT][TOPLEVEL.CMAKE] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.LICENSE] ...
	check [REQUIREMENT][TOPLEVEL.LICENSE] ... PASSED

Running check [REQUIREMENT][TOPLEVEL.README] ...
	check [REQUIREMENT][TOPLEVEL.README] ... PASSED

Running check [REQUIREMENT][CHANGELOG.TITLE] ...
[ERROR          ][CHANGELOG.TITLE          ]: The file '/Users/dariusn/dev/dn/git/Beman/exemplar/Changelog.md' does not exist.
	check [REQUIREMENT][CHANGELOG.TITLE] ... FAILED

Running check [REQUIREMENT][CHANGELOG.LIBRARY_STATUS] ...
[ERROR          ][CHANGELOG.LIBRARY_STATUS ]: CHANGELOG.md must contain a line for each previous library status with respect to the Beman library maturity model. Initial library status is missing.
	check [REQUIREMENT][CHANGELOG.LIBRARY_STATUS] ... FAILED

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


beman-tidy coverage: 17.78% (8/45 checks passed).
```
