#!/usr/bin/python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import os
import sys


class BSCheck(object):
    """
    Base class for Beman Standard check (rule).
    """

    def __init__(self, repo_info, beman_standard, check_name):
        """
        Create a new check instance.
        """
        # check name e.g. "LIBRARY.NAMES"
        self.name = check_name

        # unique entry in the list - [(check_name, check_type, check_full_text_body)]
        beman_standard_check = [
            entry for entry in beman_standard if entry[0] == check_name]
        assert len(beman_standard_check) <= 1

        # set type and full_text_body
        if len(beman_standard_check) == 1:
            (check_name, check_type, check_body) = beman_standard_check[0]

            self.type = check_type
            self.full_text_body = check_body
        else:
            self.type = "REQUIREMENT"
            self.full_text_body = "beman-tidy internal check."
        assert self.type in [
            'REQUIREMENT', 'RECOMMENDATION'], f"Invalid check type: {self.type} for check = {self.name}."
        assert self.full_text_body is not None

        self.log_level = 'ERROR' if self.type == 'REQUIREMENT' else 'WARNING'
        self.log_enabled = False

        self.repo_info = repo_info

        assert "name" in repo_info
        self.repo_name = repo_info["name"]
        assert "top_level" in repo_info
        self.repo_path = repo_info["top_level"]

        self.library_name = f"beman.{self.repo_name}"
        assert self.library_name is not None

    def base_check(self):
        """
        Checks if this rule is properly initialized.
        """
        if self.name is None:
            self.log("The name is not set.")
            return False

        if self.repo_name is None:
            self.log(f"The repo_name is not set for check = {self.name}.")
            return False

        if self.repo_path is None:
            self.log(f"The repo_path is not set for check = {self.name}.")
            return False

        return True

    def check(self):
        """
        Checks if the Beman Standard check is already applied.
        - If it's applied, this method should return True.
        - Otherwise, it returns False and self.fix() must be able to fix the issue.
        """
        raise NotImplementedError(f"[{self.name}] check() not implemented.")

    def fix(self):
        """
        Fixes the issue if the Beman Standard is not applied.
        - If check already applied, this method is a no-op and should return True.
        - Otherwise, it will try to apply the check inplace. Returns the status of the fix attempt.
        """
        return False

    def log(self, message, enabled=True):
        """
        Logs a message with the check's log level.
        e.g. [WARN][REPOSITORY.NAME]: The name "${name}" should be snake_case.'
        e.g. [ERROR][TOPLEVEL.CMAKE]: Missing top level CMakeLists.txt.'
        """

        if self.log_enabled and enabled:
            print(f'[{self.log_level:<15}][{self.name:<25}]: {message}')
