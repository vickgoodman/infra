#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import pytest
from pathlib import Path

from tests.utils.path_runners import (
    run_check_for_each_path,
)

# Actual tested checks.
from beman_tidy.lib.checks.beman_standard.toplevel import (
    ToplevelCmakeCheck,
)

test_data_prefix = "tests/lib/checks/beman_standard/toplevel/data"
valid_prefix = f"{test_data_prefix}/valid"
invalid_prefix = f"{test_data_prefix}/invalid"


def test__TOPLEVEL_CMAKE__valid(repo_info, beman_standard_check_config):
    """
    Test that repositories with CMakeLists.txt pass the check.
    """
    valid_cmake_paths = [
        Path(f"{valid_prefix}/complete_repo/"),
        Path(f"{valid_prefix}/repo_with_cmake/"),
    ]

    run_check_for_each_path(
        True,
        valid_cmake_paths,
        ToplevelCmakeCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__TOPLEVEL_CMAKE__invalid(repo_info, beman_standard_check_config):
    """
    Test that repositories without CMakeLists.txt pass the check.
    """
    invalid_cmake_paths = [
        Path(f"{invalid_prefix}/empty_repo/"),
        Path(f"{invalid_prefix}/repo_without_cmake/"),
    ]

    run_check_for_each_path(
        False,
        invalid_cmake_paths,
        ToplevelCmakeCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__TOPLEVEL_CMAKE__fix_inplace(repo_info, beman_standard_check_config):
    pass
