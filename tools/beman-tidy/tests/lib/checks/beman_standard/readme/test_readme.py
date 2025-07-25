#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import pytest
from pathlib import Path

from tests.utils.path_runners import (
    run_check_for_each_path,
    run_fix_inplace_for_each_file_path,
)

# Actual tested checks.
from beman_tidy.lib.checks.beman_standard.readme import (
    ReadmeTitleCheck,
    ReadmeBadgesCheck,
    ReadmeImplementsCheck,
    ReadmeLibraryStatusCheck,
)

test_data_prefix = "tests/lib/checks/beman_standard/readme/data"
valid_prefix = f"{test_data_prefix}/valid"
invalid_prefix = f"{test_data_prefix}/invalid"


def test__README_TITLE__valid(repo_info, beman_standard_check_config):
    """
    Test that a valid README.md title passes the check.
    """
    valid_readme_paths = [
        # Title: # beman.exemplar: A Beman Library Exemplar
        Path(f"{valid_prefix}/README-v1.md"),
        # Title: # beman.exemplar: Another Beman Library
        Path(f"{valid_prefix}/README-v2.md"),
        # Title: # beman.exemplar: Awesome Beman Library
        Path(f"{valid_prefix}/README-v3.md"),
        # Title: # beman.exemplar: The Most Awesome Beman Library
        Path(f"{valid_prefix}/README-v4.md"),
    ]

    run_check_for_each_path(
        True,
        valid_readme_paths,
        ReadmeTitleCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__README_TITLE__invalid(repo_info, beman_standard_check_config):
    """
    Test that an invalid README.md title fails the check.
    """
    invalid_readme_paths = [
        # Title: Wrong Title Format
        Path(f"{invalid_prefix}/invalid.md"),
        # Title: Missing . in beman.exemplar
        Path(f"{invalid_prefix}/invalid-title-v1.md"),
        # Title: Missing : after beman.exemplar
        Path(f"{invalid_prefix}/invalid-title-v2.md"),
        # Title: Wromg name beman.exemaplar vs beman.optional
        Path(f"{invalid_prefix}/invalid-title-v3.md"),
    ]

    run_check_for_each_path(
        False,
        invalid_readme_paths,
        ReadmeTitleCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__README_TITLE__fix_inplace(repo_info, beman_standard_check_config):
    """
    Test that the fix method corrects an invalid README.md title.
    """
    invalid_readme_paths = [
        Path(f"{invalid_prefix}/invalid-title-v1.md"),
        Path(f"{invalid_prefix}/invalid-title-v2.md"),
        Path(f"{invalid_prefix}/invalid-title-v3.md"),
    ]

    run_fix_inplace_for_each_file_path(
        invalid_readme_paths, ReadmeTitleCheck, repo_info, beman_standard_check_config
    )


def test__README_BADGES__valid(repo_info, beman_standard_check_config):
    """
    Test that a valid README.md badges passes the check.
    """
    valid_readme_paths = [
        # Badges: under development status and cpp26 target
        Path(f"{valid_prefix}/README-v1.md"),
        # Badges: production ready (api may undergo changes) status and cpp26 target
        Path(f"{valid_prefix}/README-v2.md"),
        # Badges: production ready (stable api) status and cpp29 target
        Path(f"{valid_prefix}/README-v3.md"),
        # Badges: retired status and cpp26 target
        Path(f"{valid_prefix}/README-v4.md"),
    ]

    run_check_for_each_path(
        True,
        valid_readme_paths,
        ReadmeBadgesCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__README_BADGES__invalid(repo_info, beman_standard_check_config):
    """
    Test that an invalid README.md badges fails the check.
    """
    invalid_readme_paths = [
        Path(f"{invalid_prefix}/invalid.md"),
        # Badges: typos in badge for library status
        Path(f"{invalid_prefix}/invalid-badge-v1.md"),
        # Badges: typos in badge for standard target
        Path(f"{invalid_prefix}/invalid-badge-v2.md"),
        # Badges: other description in badge for library status
        Path(f"{invalid_prefix}/invalid-badge-v3.md"),
        # Badges: other description in badge for standard target
        Path(f"{invalid_prefix}/invalid-badge-v4.md"),
        # Badges: non-sense badge for library status (broken badge URL)
        Path(f"{invalid_prefix}/invalid-badge-v5.md"),
        # Badges: non-sense badge for standard target (broken badge URL)
        Path(f"{invalid_prefix}/invalid-badge-v6.md"),
        # Badges: 1/2 badges are missing (standard target)
        Path(f"{invalid_prefix}/invalid-badge-v7.md"),
        # Badges: 1/2 badges are missing (library status)
        Path(f"{invalid_prefix}/invalid-badge-v8.md"),
    ]

    run_check_for_each_path(
        False,
        invalid_readme_paths,
        ReadmeBadgesCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__README_BADGES__fix_inplace(repo_info, beman_standard_check_config):
    """
    Test that the fix method corrects an invalid README.md badges.
    """
    # Cannot determine what badges to create. fix() is not implemented.
    pass


def test__README_IMPLEMENTS__valid(repo_info, beman_standard_check_config):
    """
    Test that a valid README.md "Implements" passes the check
    """
    valid_readme_paths = [
        Path(f"{valid_prefix}/README-v1.md"),
        Path(f"{valid_prefix}/README-v2.md"),
        Path(f"{valid_prefix}/README-v3.md"),
        Path(f"{valid_prefix}/README-v4.md"),
    ]

    run_check_for_each_path(
        True,
        valid_readme_paths,
        ReadmeImplementsCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__README_IMPLEMENTS__invalid(repo_info, beman_standard_check_config):
    """
    Test that an invalid README.md "Implements" fails the check
    """
    invalid_readme_paths = [
        Path(f"{invalid_prefix}/invalid.md"),
        Path(f"{invalid_prefix}/invalid-implements-v1.md"),
        Path(f"{invalid_prefix}/invalid-implements-v2.md"),
        Path(f"{invalid_prefix}/invalid-implements-v3.md"),
        Path(f"{invalid_prefix}/invalid-implements-v4.md"),
    ]

    run_check_for_each_path(
        False,
        invalid_readme_paths,
        ReadmeImplementsCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__README_IMPLEMENTS__fix_inplace(repo_info, beman_standard_check_config):
    """
    Test that the fix method corrects an invalid README.md "Implements".
    """
    # Cannot determine what implements to create. fix() is not implemented.
    pass


def test__README_LIBRARY_STATUS__valid(repo_info, beman_standard_check_config):
    """
    Test that a valid README.md library status passes the check.
    """
    valid_readme_paths = [
        Path(f"{valid_prefix}/README-v1.md"),
        Path(f"{valid_prefix}/README-v2.md"),
        Path(f"{valid_prefix}/README-v3.md"),
        Path(f"{valid_prefix}/README-v4.md"),
    ]

    run_check_for_each_path(
        True,
        valid_readme_paths,
        ReadmeLibraryStatusCheck,
        repo_info,
        beman_standard_check_config,
    )


def test__README_LIBRARY_STATUS__invalid(repo_info, beman_standard_check_config):
    """
    Test that an invalid README.md library status fails the check.
    """
    invalid_readme_paths = [
        Path(f"{invalid_prefix}/invalid.md"),
        Path(f"{invalid_prefix}/invalid-status-line-v1.md"),
        Path(f"{invalid_prefix}/invalid-status-line-v2.md"),
        Path(f"{invalid_prefix}/invalid-status-line-v3.md"),
    ]

    run_check_for_each_path(
        False,
        invalid_readme_paths,
        ReadmeLibraryStatusCheck,
        repo_info,
        beman_standard_check_config,
    )


@pytest.mark.skip(reason="NOT implemented")
def test__README_LIBRARY_STATUS__fix_inplace(repo_info, beman_standard_check_config):
    """
    Test that the fix method corrects an invalid README.md library status.
    """
    # Cannot determine what library status to create. fix() is not implemented.
    pass
