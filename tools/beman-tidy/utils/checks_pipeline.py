#!/usr/bin/python3
# SPDX-License-Identifier: 2.0 license with LLVM exceptions

from .beman_standard_checks import *


def get_all_implemented_checks():
    """
    Get the checks pipeline - it is a list of checks, that need to be run.
    The list may contain checks that are not from The Beman Standard.

    Returns a list of checks that need to be run.
    """
    return [
        # Validate CLI arguments
        BSCheckFixInplaceIncompatibleWithUnstagedChanges,

        # Validate ...
    ]


def get_beman_standard_check(beman_standard, check_name):
    """
    Get The Beman Standard check object from the Beman Standard that matches the check_name.
    """
    return next(filter(lambda bs_check: bs_check[0] == check_name, beman_standard), None)


def run_checks_pipeline(repo_info, beman_standard, fix_inplace=False, coverage=False):
    """
    Run the checks pipeline for The Beman Standard.
    If fix_inplace is True, fix the issues inplace.
    If coverage is True, print the coverage.
    """

    print("Checks pipeline started ...\n")
    for generic_check in get_all_implemented_checks():
        bs_check = generic_check(repo_info, beman_standard)
        print(
            f"Running check [{bs_check.type}][{bs_check.name}] ... ")

        if bs_check.check():
            print(f"\tcheck [{bs_check.type}][{bs_check.name}] ... PASSED\n")
        else:
            print(f"\tcheck [{bs_check.type}][{bs_check.name}] ... FAILED\n")

            if fix_inplace:
                if bs_check.fix():
                    bs_check.log(f"\tcheck '{bs_check.name}' ... FIXED.")
                else:
                    bs_check.log(
                        f"\tcheck '{bs_check.name}' ... FAILED TO FIX INPLACE. Please manually fix it!")

    print("\nChecks pipeline completed.")

    if coverage:
        print_coverage(repo_info, beman_standard)


def print_coverage(repo_info, beman_standard):
    """
    Print The Beman Standard coverage.
    """
    # Actual implemented checks.
    all_implemented_checks = [generic_check(
        repo_info, beman_standard) for generic_check in get_all_implemented_checks()]
    bs_implemented_checks = [generic_check for generic_check in all_implemented_checks if get_beman_standard_check(
        beman_standard, generic_check.name)]
    passed_bs_checks = [
        bs_check for bs_check in bs_implemented_checks if bs_check.check()]

    # Stats about the clang-tidy checks coverage over The Beman Standard.
    total_bs_hecks = len(beman_standard)
    total_implemented_bs_checks = len([generic_check for generic_check in get_all_implemented_checks(
    ) if get_beman_standard_check(beman_standard, generic_check(repo_info, beman_standard))])

    print(
        f"repo coverage over The Beman Standard: {len(passed_bs_checks) / total_bs_hecks * 100}% ({len(passed_bs_checks)}/{total_bs_hecks} checks passed).")
    print(
        f"clang-tidy coverage over The Beman Standard: {total_implemented_bs_checks / total_bs_hecks * 100}% ({total_implemented_bs_checks}/{total_bs_hecks} checks implemented).")
