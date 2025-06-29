#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from .cmake import CMakeBaseCheck
from ..base.file_base_check import FileBaseCheck
from .readme import ReadmeBaseCheck
from ..system.registry import register_beman_standard_check

# [TOPLEVEL.*] checks category.
# All checks in this file extend the ToplevelBaseCheck class.
#
# Note: ToplevelBaseCheck is not a registered check!


@register_beman_standard_check(check="TOPLEVEL.CMAKE")
class ToplevelCmakeCheck(CMakeBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        return super().pre_check()

    def fix(self):
        # TODO: Implement the fix.
        pass

@register_beman_standard_check("TOPLEVEL.LICENSE")
class ToplevelLicenseCheck(FileBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        self.path = self.repo_path / self.config["file_name"]

        if not self.path.exists():
            self.log("The LICENSE file does not exist.")
            return False

        try:
            with open(self.path, 'r') as file:
                if len(file.read()) == 0:
                    self.log("The LICENSE file is empty.")
                    return False
        except Exception:
            self.log("Failed to read the LICENSE file.")
            return False

        return True
    
    def fix(self):
        # TODO: Implement the fix.
        pass

@register_beman_standard_check("TOPLEVEL.README")
class ToplevelReadmeCheck(ReadmeBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        self.path = self.repo_path / self.config["file_name"]

        if not self.path.exists():
            self.log("The README file does not exist.")
            return False

        try:
            with open(self.path, 'r') as file:
                if len(file.read()) == 0:
                    self.log("The README file is empty.")
                    return False
        except Exception:
            self.log("Failed to read the README file.")
            return False

        return True
    
    def fix(self):
        # TODO: Implement the fix.
        pass

