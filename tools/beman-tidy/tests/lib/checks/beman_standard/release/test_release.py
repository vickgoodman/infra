#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import pytest
from pathlib import Path

from tests.utils.path_runners import (
    run_check_for_each_path,
)

# Actual tested checks.
from beman_tidy.lib.checks.beman_standard.release import (
    ReleaseGodboltTrunkVersionCheck,
)

test_data_prefix = "tests/lib/checks/beman_standard/release/data"
valid_prefix = f"{test_data_prefix}/valid"
invalid_prefix = f"{test_data_prefix}/invalid"


def test__RELEASE_GODBOLT_TRUNK_VERSION__valid(repo_info, beman_standard_check_config):
    """
    Test that repositories with present Godbolt trunk version pass the check.
    """
    valid_godbolt_trunk_version_paths = [
        # exemplar/ repo with root README.md containing valid Godbolt trunk version.
        Path(f"{valid_prefix}/repo-exemplar-v1/"),
    ]

    run_check_for_each_path(
        True,
        valid_godbolt_trunk_version_paths,
        ReleaseGodboltTrunkVersionCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__RELEASE_GODBOLT_TRUNK_VERSION__invalid(
    repo_info, beman_standard_check_config
):
    """
    Test that repositories with missing Godbolt trunk version fail the check.
    """
    invalid_godbolt_trunk_version_paths = [
        # exemplar/ repo root README.md without Godbolt trunk version.
        Path(f"{invalid_prefix}/repo-exemplar-v1/"),
    ]

    run_check_for_each_path(
        False,
        invalid_godbolt_trunk_version_paths,
        ReleaseGodboltTrunkVersionCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__RELEASE_GODBOLT_TRUNK_VERSION__fix_inplace(
    repo_info, beman_standard_check_config
):
    pass
