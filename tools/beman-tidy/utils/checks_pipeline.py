#!/usr/bin/python3
# SPDX-License-Identifier: 2.0 license with LLVM exceptions

from .beman_standard_checks import *


def get_checks_pipeline(repo_info):
    """
    Get the checks pipeline for The Beman Standard.
    Returns a list of checks that need to be run.
    """
    return [
        # Validate CLI arguments
        BSCheckFixInplaceIncompatibleWithUnstagedChanges,

        # Validate ...
    ]


def run_checks_pipeline(fix_inplace, repo_info):
    """
    Run the checks pipeline for The Beman Standard.
    If fix_inplace is True, fix the issues inplace.
    """

    print("Checks pipeline started ...\n")
    checks_pipeline = get_checks_pipeline(repo_info)
    for bs_check_type in checks_pipeline:
        bs_check = bs_check_type(repo_info)
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
