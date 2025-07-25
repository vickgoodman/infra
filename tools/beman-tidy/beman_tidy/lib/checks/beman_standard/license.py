#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import re
import filecmp
import textwrap

from ..base.base_check import BaseCheck
from ..base.file_base_check import FileBaseCheck
from ..system.registry import register_beman_standard_check
from beman_tidy.lib.utils.git import get_beman_recommendated_license_path

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
        content = self.read()

        # Regex for LICENSE check
        # - fixed header matching
        # - non empty body matching
        # - fixed footer matching
        regex = re.compile(
            textwrap.dedent(r"""
                ^={78}
                The Beman Project is under the (Apache License v2\.0 with LLVM Exceptions|Boost Software License 1\.0|MIT License):
                ={78}

                (.+?)

                ={78}
                Software from third parties included in the Beman Project:
                ={78}
                The Beman Project contains third party software which is under different license
                terms\. All such code will be identified clearly using at least one of two
                mechanisms:
                1\) It will be in a separate directory tree with its own `LICENSE\.txt` or
                   `LICENSE` file at the top containing the specific license and restrictions
                   which apply to that software, or
                2\) It will contain specific license and restriction terms at the top of every
                   file\.
                """).strip(),
            re.DOTALL,
        )

        if not regex.match(content):
            self.log(
                "LICENSE file does not match the required format. "
                "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
            )
            return False

        return True

    def fix(self):
        self.log(
            "Please update the LICENSE file to include an approved license. "
            "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
        )


@register_beman_standard_check("LICENSE.APACHE_LLVM")
class LicenseApacheLLVMCheck(LicenseBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        # Compare LICENSE file stored at self.path with the reference one.
        target_license = self.path
        ref_license = get_beman_recommendated_license_path()
        if not filecmp.cmp(target_license, ref_license, shallow=False):
            self.log(
                "Please update the LICENSE file to include the Apache License v2.0 with LLVM Exceptions. "
                "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapache_llvm for more information."
            )
            return False

        return True

    def fix(self):
        self.log(
            "Please update the LICENSE file to include the Apache License v2.0 with LLVM Exceptions. "
            "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapache_llvm for more information."
        )


@register_beman_standard_check("LICENSE.CRITERIA")
class LicenseCriteriaCheck(BaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def should_skip(self):
        # Cannot actually implement LICENSE.CRITERIA, so skip it.
        # No need to run pre_check() and check() as well, as they are not implemented.
        self.log(
            "beman-tidy cannot actually check LICENSE.CRITERIA. Please ignore this message if LICENSE.APPROVED has passed. "
            "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licensecriteria for more information."
        )
        return True

    def check(self):
        # Check should_skip(). Stub provided to be able to instantiate the check.
        return True

    def fix(self):
        # Check should_skip().
        return True
