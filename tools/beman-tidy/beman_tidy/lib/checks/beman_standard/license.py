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

        separator_line = "=============================================================================="
        approved_licenses = [
            "Apache License v2.0 with LLVM Exceptions",
            "Boost Software License 1.0",
            "MIT License",
        ]

        # Check if license header is correct
        license_header = lines[0:3]

        has_approved_license_header = False
        for approved_license in approved_licenses:
            if (
                license_header[0] == separator_line
                and license_header[1]
                == f"The Beman Project is under the {approved_license}:"
                and license_header[2] == separator_line
            ):
                has_approved_license_header = True

        if has_approved_license_header == False:
            self.log(
                "Incorrect header for LICENSE. "
                "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
            )
            return False

        # Check if license footer is correct
        license_footer = lines[-11:]

        correct_license_footer = [
            "==============================================================================",
            "Software from third parties included in the Beman Project:",
            "==============================================================================",
            "The Beman Project contains third party software which is under different license",
            "terms. All such code will be identified clearly using at least one of two",
            "mechanisms:",
            "1) It will be in a separate directory tree with its own `LICENSE.txt` or",
            "`LICENSE` file at the top containing the specific license and restrictions",
            "which apply to that software, or",
            "2) It will contain specific license and restriction terms at the top of every",
            "file.",
        ]

        if license_footer != correct_license_footer:
            self.log(
                "Incorrect footer for LICENSE. "
                "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
            )
            return False

        # Check if there's any content between the header and footer
        if len(lines) < 17:
            self.log(
                "LICENSE contains only footer and header. There should be actual license content. "
                "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
            )
            return False

        return True

    def fix(self):
        self.log(
            "Please update the LICENSE file to include an approved license. "
            "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
        )


# TODO LICENSE.APACHE_LLVM


# TODO LICENSE.CRITERIA
