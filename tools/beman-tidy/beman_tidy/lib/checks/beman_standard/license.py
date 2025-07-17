#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from ..base.file_base_check import FileBaseCheck
from ..system.registry import register_beman_standard_check
import re
import textwrap


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
        license_text = self.read()

        pattern = re.compile(
            textwrap.dedent(r"""
            ^={78}\n
            The Beman Project is under the
                (Apache License v2\.0 with LLVM Exceptions|
                Boost Software License 1\.0|
                MIT License):
            \n={78}\n

            (.+?)  # Non-empty license body

            ={78}\n
            Software from third parties included in the Beman Project:\n
            ={78}\n
            The Beman Project contains third party software which is under different license
            terms\. All such code will be identified clearly using at least one of two
            mechanisms:\n
            1\) It will be in a separate directory tree with its own `LICENSE\.txt` or
            `LICENSE` file at the top containing the specific license and restrictions
            which apply to that software, or\n
            2\) It will contain specific license and restriction terms at the top of every
            file\.
        """),
            re.DOTALL | re.VERBOSE,
        )

        if not pattern.match(license_text):
            self.log(
                "The LICENSE file does not contain an approved license. "
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
