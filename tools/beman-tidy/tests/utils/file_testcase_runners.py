#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import os
from pathlib import Path

# This file contains the testcase runners for the file-based checks.
# Some of the runners use a single file, while others use multiple files.
# The runners are named:
# - file_testcase_run
# - file_testcase_run_<expected_result>
# - file_testcases_run_<expected_result>
# - file_testcase_run_fix_inplace
# - file_testcases_run_fix_inplace


def file_testcase_run(
    file_path, check_class, repo_info, beman_standard_check_config, expected_result
):
    """
    Run a testcase for a file-based check.

    Example:
        file_path = "tests/lib/checks/beman_standard/readme/data/valid/README-v1.md"
        check_class = ReadmeTitleCheck
        repo_info = "beman.exemplar"
        beman_standard_check_config = "beman_tidy/.beman-standard.yml"
        expected_result = True
    """
    check_instance = check_class(repo_info, beman_standard_check_config)
    check_instance.path = Path(file_path)
    check_instance.log_level = True

    assert check_instance.pre_check() is True, (
        f"[{check_instance.__class__.__name__}] pre_check() failed for {file_path}"
    )
    assert check_instance.check() is expected_result, (
        f"[{check_instance.__class__.__name__}] check() failed for {file_path}"
    )


def file_testcases_run(
    file_paths, check_class, repo_info, beman_standard_check_config, expected_result
):
    """
    Run multiple testcases for a file-based check.

    Example: Similar to file_testcase_run(), but with multiple file_paths.
    """
    for file_path in file_paths:
        file_testcase_run(
            file_path,
            check_class,
            repo_info,
            beman_standard_check_config,
            expected_result,
        )


def file_testcase_run_valid(
    file_path, check_class, repo_info, beman_standard_check_config
):
    """
    Run a testcase for a file-based check.

    Example: Similar to file_testcase_run(), but with expected_result = True.
    """
    file_testcase_run(
        file_path, check_class, repo_info, beman_standard_check_config, True
    )


def file_testcase_run_invalid(
    file_path, check_class, repo_info, beman_standard_check_config
):
    """
    Run a testcase for a file-based check.

    Example: Similar to file_testcase_run(), but with expected_result = False.
    """
    file_testcase_run(
        file_path, check_class, repo_info, beman_standard_check_config, False
    )



def file_testcases_run_valid(
    file_paths, check_class, repo_info, beman_standard_check_config
):
    """
    Run multiple testcases for a file-based check.

    Example:
        file_paths = [
            "tests/lib/checks/beman_standard/readme/data/valid/README-v1.md",
            "tests/lib/checks/beman_standard/readme/data/valid/README-v2.md",
        ]
        check_class = ReadmeTitleCheck
        repo_info = "beman.exemplar"
        beman_standard_check_config = "beman_tidy/.beman-standard.yml"
    """
    file_testcases_run(
        file_paths, check_class, repo_info, beman_standard_check_config, True
    )


def file_testcases_run_invalid(
    file_paths, check_class, repo_info, beman_standard_check_config
):
    """
    Run multiple testcases for a file-based check.

    Example:
        file_paths = [
            "tests/lib/checks/beman_standard/readme/data/invalid/README-v1.md",
            "tests/lib/checks/beman_standard/readme/data/invalid/README-v2.md",
        ]
        check_class = ReadmeTitleCheck
        repo_info = "beman.exemplar"
        beman_standard_check_config = "beman_tidy/.beman-standard.yml"
    """
    file_testcases_run(
        file_paths, check_class, repo_info, beman_standard_check_config, False
    )

def file_testcase_run_fix_inplace(
    invalid_file_path, check_class, repo_info, beman_standard_check_config
):
    """
    Run a testcase for a file-based check, starting with a file that is invalid,
    and then fixing it.

    Example:
        invalid_file_path = "tests/lib/checks/beman_standard/readme/data/invalid/README-v1.md"
        check_class = ReadmeTitleCheck
        repo_info = "beman.exemplar"
        beman_standard_check_config = "beman_tidy/.beman-standard.yml"
    """
    check_instance = check_class(repo_info, beman_standard_check_config)
    check_instance.path = Path(f"{invalid_file_path}.delete_me")
    check_instance.write(invalid_file_path.read_text())

    assert check_instance.pre_check() is True
    assert check_instance.check() is False

    assert check_instance.fix() is True

    assert check_instance.pre_check() is True
    assert check_instance.check() is True

    # Delete the temporary file
    os.remove(f"{invalid_file_path}.delete_me")


def file_testcases_run_fix_inplace(
    invalid_file_paths, check_class, repo_info, beman_standard_check_config
):
    """
    Run multiple testcases for a file-based check, for each file starting with a file that is invalid,
    and then fixing it.

    Example:
        invalid_file_paths = [
            "tests/lib/checks/beman_standard/readme/data/invalid/README-v1.md",
            "tests/lib/checks/beman_standard/readme/data/invalid/README-v2.md",
        ]
        check_class = ReadmeTitleCheck
        repo_info = "beman.exemplar"
        beman_standard_check_config = "beman_tidy/.beman-standard.yml"
    """
    for invalid_file_path in invalid_file_paths:
        file_testcase_run_fix_inplace(
            invalid_file_path, check_class, repo_info, beman_standard_check_config
        )
