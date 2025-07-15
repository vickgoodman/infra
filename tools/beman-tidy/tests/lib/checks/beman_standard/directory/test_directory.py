#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import pytest
from pathlib import Path

from tests.utils.path_runners import (
    run_check_for_each_path,
)

# Actual tested checks.
from beman_tidy.lib.checks.beman_standard.directory import (
    DirectoryInterfaceHeadersCheck,
)

test_data_prefix = "tests/lib/checks/beman_standard/directory/data"
valid_prefix = f"{test_data_prefix}/valid"
invalid_prefix = f"{test_data_prefix}/invalid"


def test__DIRECTORY_INTERFACE_HEADERS__valid(repo_info, beman_standard_check_config):
    """
    Test that repositories with valid public header files pass the check.
    """
    valid_headers_paths = [
        # exemplar/ repo with valid public headers.
        Path(f"{valid_prefix}/repo-exemplar-v1/"),
    ]

    run_check_for_each_path(
        True,
        valid_headers_paths,
        DirectoryInterfaceHeadersCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__DIRECTORY_INTERFACE_HEADERS__invalid(repo_info, beman_standard_check_config):
    """
    Test that repositories with invalid public header files fail the check.
    """
    invalid_headers_paths = [
        # exemplar/ repo without include/beman/<short_name>/ directory.
        Path(f"{invalid_prefix}/repo-exemplar-v1/"),
        # exemplar/ repo with include/beman/<short_name>/ directory but no public headers.
        Path(f"{invalid_prefix}/repo-exemplar-v2/"),
        # exemplar/ repo with public headers outside include/beman/<short_name>/ directory.
        Path(f"{invalid_prefix}/repo-exemplar-v3/"),
    ]

    run_check_for_each_path(
        False,
        invalid_headers_paths,
        DirectoryInterfaceHeadersCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__DIRECTORY_INTERFACE_HEADERS__fix_inplace(
    repo_info, beman_standard_check_config
):
    pass
