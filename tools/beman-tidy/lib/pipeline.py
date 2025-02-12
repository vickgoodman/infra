#!/usr/bin/python3
# SPDX-License-Identifier: 2.0 license with LLVM exceptions

from .checks.system.git import *
from .checks.beman_standard.changelog import *
from .checks.beman_standard.cmake import *
from .checks.beman_standard.cpp import *
from .checks.beman_standard.directory import *
from .checks.beman_standard.file import *
from .checks.beman_standard.general import *
from .checks.beman_standard.license import *
from .checks.beman_standard.readme import *
from .checks.beman_standard.toplevel import *


def get_all_implemented_checks():
    """
    Get the checks pipeline - it is a list of checks, that need to be run.
    The list may contain checks that are not from The Beman Standard.

    Returns a list of checks that need to be run.
    """
    return [
        # Validate CLI arguments
        BSCheckFixInplaceIncompatibleWithUnstagedChanges,

        # TOPLEVEL
        BSTopLevelChangelogCheck,
        BSTopLevelCMakeListsCheck,
        BSTopLevelLicenseCheck,
        BSTopLevelREADMECheck,

        # CHANGELOG
        BSChangelogTitleCheck,
        BSChangelogLibraryStatus,

        # README
        BSReadmeTitleCheck,
        BSReadmeBadgesCheck,
        # PURPOSE
        BSReadmeImplementsCheck,
        BSReadmeLibraryStatusCheck,
    ]


def get_beman_standard_check(beman_standard, check_name):
    """
    Get The Beman Standard check object from the Beman Standard that matches the check_name.
    """
    return next(filter(lambda bs_check: bs_check[0] == check_name, beman_standard), None)


def run_checks_pipeline(repo_info, beman_standard, fix_inplace=False, verbose=False):
    """
    Run the checks pipeline for The Beman Standard.
    Read-only checks if fix_inplace is False, otherwise try to fix the issues in-place.
    """
    def log(msg):
        if verbose:
            print(msg)

    log("beman-tidy started ...\n")
    for generic_check in get_all_implemented_checks():
        bs_check = generic_check(repo_info, beman_standard)
        bs_check.log_enabled = verbose

        log(
            f"Running check [{bs_check.type}][{bs_check.name}] ... ")

        if not fix_inplace:
            if bs_check.base_check() and bs_check.check():
                log(f"\tcheck [{bs_check.type}][{bs_check.name}] ... PASSED\n")
            else:
                log(f"\tcheck [{bs_check.type}][{bs_check.name}] ... FAILED\n")
        else:
            if bs_check.fix():
                log(f"\tcheck '{bs_check.name}' ... (already) FIXED.")
            else:
                log(
                    f"\tcheck '{bs_check.name}' ... FAILED TO FIX INPLACE. Please manually fix it!")

    log("\nbeman-tidy finished.\n")
    sys.stdout.flush()


def print_coverage(repo_info, beman_standard):
    """
    Print The Beman Standard coverage.
    """
    all_implemented_checks = [generic_check(
        repo_info, beman_standard) for generic_check in get_all_implemented_checks()]
    all_bs_implemented_checks = [check for check in all_implemented_checks if get_beman_standard_check(
        beman_standard, check.name) is not None]
    passed_bs_checks = [
        check for check in all_bs_implemented_checks if check.base_check() and check.check()]
    coverage = round(len(passed_bs_checks) / len(beman_standard) * 100, 2)

    # print(f"(beman-tidy implementation status: {len(all_bs_implemented_checks)}/{len(beman_standard)} checks implemented.)")
    print(
        f"\nbeman-tidy coverage: {coverage}% ({len(passed_bs_checks)}/{len(beman_standard)} checks passed).")
