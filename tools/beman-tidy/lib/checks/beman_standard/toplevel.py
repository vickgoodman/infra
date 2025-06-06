#!/usr/bin/python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from ..base.file_base_check import FileBaseCheck
from ...utils.git import *

class BSTopLevelCMakeListsCheck(FileBaseCheck):
    def __init__(self, repo_info, beman_standard):
        super().__init__(repo_info, beman_standard, "TOPLEVEL.CMAKE", "CMakeLists.txt")

    def check(self):
        return super().default_check()  # Non-empty file check.

    def fix(self):
        # TODO import from beman_standard.
        pass


class BSTopLevelLicenseCheck(FileBaseCheck):
    def __init__(self, repo_info, beman_standard):
        super().__init__(repo_info, beman_standard, "TOPLEVEL.LICENSE", "LICENSE")

    def check(self):
        return super().default_check()  # Non-empty file check.

    def fix(self):
        # TODO import from beman_standard.
        self.write(download_beman_default_license())
        pass


class BSTopLevelREADMECheck(FileBaseCheck):
    def __init__(self, repo_info, beman_standard):
        super().__init__(repo_info, beman_standard, "TOPLEVEL.README", "README.md")

    def check(self):
        return super().default_check()  # Non-empty file check.

    def fix(self):
        # TODO import from beman_standard.
        pass
