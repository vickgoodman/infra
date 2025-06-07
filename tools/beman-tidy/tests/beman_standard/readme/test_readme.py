#!/usr/bin/python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import pytest
from pathlib import Path
from lib.checks.beman_standard.readme import ReadmeTitleCheck


def test_valid_readme_title(repo_info, beman_standard_check_config, valid_readme_path):
    """Test that a valid README.md title passes the check"""
    check_instance = ReadmeTitleCheck(repo_info, beman_standard_check_config)
    check_instance.path = valid_readme_path

    assert check_instance.default_check() is True
    assert check_instance.check() is True


def test_invalid_readme_title(repo_info, beman_standard_check_config, invalid_readme_path):
    """Test that an invalid README.md title fails the check"""
    check_instance = ReadmeTitleCheck(repo_info, beman_standard_check_config)
    check_instance.path = invalid_readme_path

    assert check_instance.default_check() is True
    assert check_instance.check() is False


def test_fix_invalid_readme_title(repo_info, beman_standard_check_config, invalid_readme_path, valid_readme_path):
    """Test that the fix method corrects an invalid README.md title"""
    check_instance = ReadmeTitleCheck(repo_info, beman_standard_check_config)
    check_instance.path = f"{invalid_readme_path}.delete_me"
    check_instance.write(invalid_readme_path.read_text())

    assert check_instance.default_check() is True
    assert check_instance.check() is False

    assert check_instance.fix() is True

    assert check_instance.default_check() is True
    assert check_instance.check() is True
