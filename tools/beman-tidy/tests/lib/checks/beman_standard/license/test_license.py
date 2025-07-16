#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import pytest
from pathlib import Path

from tests.utils.path_runners import (
    run_check_for_each_path,
    run_fix_inplace_for_each_file_path,
)

# Actual tested checks.
from beman_tidy.lib.checks.beman_standard.license import (
    LicenseApprovedCheck,
)

test_data_prefix = "tests/lib/checks/beman_standard/license/data"
valid_prefix = f"{test_data_prefix}/valid"
invalid_prefix = f"{test_data_prefix}/invalid"


def test__LICENSE_APPROVED__valid(repo_info, beman_standard_check_config):
    """
    Test that a valid LICENSE file passes the check.
    """
    valid_license_paths = [
        # Apache License 2.0
        Path(f"{valid_prefix}/LICENSE-v1"),
        # Boost Software License 1.0
        Path(f"{valid_prefix}/LICENSE-v2"),
        # MIT License
        Path(f"{valid_prefix}/LICENSE-v3"),
    ]

    run_check_for_each_path(
        True,
        valid_license_paths,
        LicenseApprovedCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__LICENSE_APPROVED__invalid(repo_info, beman_standard_check_config):
    """
    Test that an invalid LICENSE file fails the check.
    """
    invalid_license_paths = [
        # GNU General Public License (GPL) v3.0
        Path(f"{invalid_prefix}/invalid-LICENSE-v1"),
        # GNU Lesser General Public License (LGPL) v3.0
        Path(f"{invalid_prefix}/invalid-LICENSE-v2"),
        # BSD-2-Clause License
        Path(f"{invalid_prefix}/invalid-LICENSE-v3"),
    ]

    run_check_for_each_path(
        False,
        invalid_license_paths,
        LicenseApprovedCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__LICENSE_APPROVED__fix_inplace(repo_info, beman_standard_check_config):
    pass
