#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import pytest
from pathlib import Path

from tests.utils.path_runners import (
    run_check_for_each_path,
)

# Actual tested checks.
from beman_tidy.lib.checks.beman_standard.release import (
    ReleaseGithubCheck,
    ReleaseGodboltTrunkVersionCheck,
    ReleaseNotesCheck,
)

test_data_prefix = "tests/lib/checks/beman_standard/release/data"
valid_prefix = f"{test_data_prefix}/valid"
invalid_prefix = f"{test_data_prefix}/invalid"


def test__RELEASE_GITHUB__valid(repo_info, beman_standard_check_config):
    """
    Test that repositories with GitHub release pass the check.
    """
    valid_repo_paths = [
        # RELEASE.GITHUB always passes, as beman-tidy is an offline tool.
        Path(f"{valid_prefix}/repo-exemplar-v1/"),
        Path(f"{invalid_prefix}/repo-exemplar-v1/"),
    ]

    run_check_for_each_path(
        True,
        valid_repo_paths,
        ReleaseGithubCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__RELEASE_GITHUB__invalid(repo_info, beman_standard_check_config):
    """
    Test that repositories with missing GitHub release fail the check.
    """
    # RELEASE.GITHUB always passes, as beman-tidy is an offline tool.
    pass


@pytest.mark.skip(reason="NOT implemented")
def test__RELEASE_GITHUB__fix_inplace(repo_info, beman_standard_check_config):
    # RELEASE.GITHUB always passes, as beman-tidy is an offline tool.
    pass


def test__RELEASE_NOTES__valid(repo_info, beman_standard_check_config):
    """
    Test that repositories with release notes pass the check.
    """
    valid_repo_paths = [
        # RELEASE.NOTES always passes, as beman-tidy is an offline tool.
        Path(f"{valid_prefix}/repo-exemplar-v1/"),
        Path(f"{invalid_prefix}/repo-exemplar-v1/"),
    ]

    run_check_for_each_path(
        True,
        valid_repo_paths,
        ReleaseNotesCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__RELEASE_NOTES__invalid(repo_info, beman_standard_check_config):
    """
    Test that repositories with missing release notes fail the check.
    """
    # RELEASE.NOTES always passes, as beman-tidy is an offline tool.
    pass


@pytest.mark.skip(reason="NOT implemented")
def test__RELEASE_NOTES__fix_inplace(repo_info, beman_standard_check_config):
    """
    Test that repositories with missing release notes fail the check.
    """
    # RELEASE.NOTES always passes, as beman-tidy is an offline tool.
    pass


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
    """
    Test that the fix method corrects an invalid README.md Godbolt trunk version.
    """
    # Cannot determine what Godbolt trunk version to create. fix() is not implemented.
    pass
