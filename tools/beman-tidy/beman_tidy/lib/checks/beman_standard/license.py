#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import re
import filecmp

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

        def match_apache_license_v2_with_llvm_exceptions(content):
            # beman/LICENSE contains the following text (multiple lines)
            # - Apache License
            # - Version 2.0
            # - LLVM Exceptions to the Apache 2.0 License
            #
            # We also check for variations.
            #
            license_regex = [
                rf"Apache License",  # noqa: F541
                rf"Apache License 2\.0 with LLVM Exceptions",  # noqa: F541
            ]
            if not any(
                re.search(regex, content, re.IGNORECASE) is not None
                for regex in license_regex
            ):
                return False

            version_regex = [
                rf"Version 2\.0",  # noqa: F541,
                rf"Version 2\.0 with LLVM Exceptions",  # noqa: F541,
                rf"Apache 2\.0",  # noqa: F541,
            ]
            if not any(
                re.search(regex, content, re.IGNORECASE) is not None
                for regex in version_regex
            ):
                return False

            llvm_exceptions_regex = [
                rf"LLVM Exceptions",  # noqa: F541,
                rf"Apache License 2\.0 with LLVM Exceptions",  # noqa: F541,
                rf"LLVM Exceptions to the Apache 2\.0 License",  # noqa: F541,
            ]
            if not any(
                re.search(regex, content, re.IGNORECASE) is not None
                for regex in llvm_exceptions_regex
            ):
                return False

            return True

        def match_boost_software_license_v1_0(content):
            # beman/LICENSE contains the following text (multiple lines)
            # - Boost Software License
            # - Version 1.0
            #
            # We also check for variations.
            #
            license_regex = [
                rf"Boost Software License",  # noqa: F541
                rf"Boost License",  # noqa: F541
            ]
            if not any(
                re.search(regex, content, re.IGNORECASE) is not None
                for regex in license_regex
            ):
                return False

            version_regex = [
                rf"Version 1\.0",  # noqa: F541,
                rf"V1\.0",  # noqa: F541,
            ]
            if not any(
                re.search(regex, content, re.IGNORECASE) is not None
                for regex in version_regex
            ):
                return False

            return True

        def match_the_mit_license(content):
            # beman/LICENSE contains the following text (multiple lines)
            # - The MIT License
            #
            # We also check for variations.
            #
            license_regex = [
                rf"The MIT License",  # noqa: F541
                rf"MIT License",  # noqa: F541
            ]
            if not any(
                re.search(regex, content, re.IGNORECASE) is not None
                for regex in license_regex
            ):
                return False

            return True

        if match_apache_license_v2_with_llvm_exceptions(content):
            self.log(
                "Valid Apache License - Version 2.0 with LLVM Exceptions found in LICENSE file.",
                log_level="INFO",
            )
            return True

        if match_boost_software_license_v1_0(content):
            self.log(
                "Valid Boost Software License - Version 1.0 found in LICENSE file.",
                log_level="INFO",
            )
            return True

        if match_the_mit_license(content):
            self.log("Valid MIT License found in LICENSE file.", log_level="INFO")
            return True

        self.log(
            "Invalid license - cannot find approved license in LICENSE file. "
            "See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#licenseapproved for more information."
        )
        return False

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
