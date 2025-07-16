#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from ..base.file_base_check import FileBaseCheck
from ..system.registry import register_beman_standard_check


# [LICENSE.*] checks category.
# All checks in this file extend the LicenseBaseCheck class.
#
# Note: LicenseBaseCheck is not a registered check!


class LicenseBaseCheck(FileBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config, "LICENSE")


@register_beman_standard_check("LICENSE.APPROVED")
class LicenseApprovedCheck(LicenseBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        lines = self.read_lines_strip()

        approved_licenses = ["Apache License", "Boost Software License", "MIT License"]

        for line in lines:
            if any(license_name in line for license_name in approved_licenses):
                return True

        self.log(
            f"The file '{self.path}' does not contain an approved license. "
            "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
        )
        return False

    def fix(self):
        self.log(
            "Please update the LICENSE file to include an approved license. "
            "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
        )


# TODO LICENSE.APACHE_LLVM


# TODO LICENSE.CRITERIA
