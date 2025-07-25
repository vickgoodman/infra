#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import re
from beman_tidy.lib.checks.base.base_check import BaseCheck
from beman_tidy.lib.checks.beman_standard.readme import ReadmeBaseCheck
from ..system.registry import register_beman_standard_check

# [RELEASE.*] checks category.
# Note: Data is stored online - e.g. https://github.com/bemanproject/exemplar/releases
# beman-tidy is an offline tool, so it cannot check these issues,
# but for some of them it will try some heuristics.


@register_beman_standard_check("RELEASE.GITHUB")
class ReleaseGithubCheck(BaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        # Need to always return True, as beman-tidy is an offline tool
        # that does not have access to the GitHub API.
        self.log(
            "beman-tidy cannot check this issue. See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#releasegithub."
        )
        return True

    def fix(self):
        self.log(
            "beman-tidy cannot fix this issue. See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#releasegithub."
        )


# TODO RELEASE.NOTES
@register_beman_standard_check("RELEASE.NOTES")
class ReleaseNotesCheck(BaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        # Need to always return True, as beman-tidy is an offline tool
        # that does not have access to the GitHub API.
        self.log(
            "beman-tidy cannot check this issue. See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#releasenotes."
        )
        return True

    def fix(self):
        self.log(
            "beman-tidy cannot fix this issue. See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#releasenotes."
        )


@register_beman_standard_check("RELEASE.GODBOLT_TRUNK_VERSION")
class ReleaseGodboltTrunkVersionCheck(ReadmeBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        """
        Check that the Godbolt badge is present in the root README.md file.
        If present, this assumes that the trunk version is available on Godbolt.

        e.g. [![Compiler Explorer Example](https://img.shields.io/badge/Try%20it%20on%20Compiler%20Explorer-grey?logo=compilerexplorer&logoColor=67c52a)](https://godbolt.org/z/Gc6Y9j6zf)
        Note: Only the suffix of the https://godbolt.org/z/* has dynamic content.
        """

        content = self.read()
        regex = re.compile(
            r"\[!\[Compiler Explorer Example\]\(https://img\.shields\.io/badge/Try%20it%20on%20Compiler%20Explorer-grey\?logo=compilerexplorer&logoColor=67c52a\)\]\(https://godbolt\.org/z/([a-zA-Z0-9]+)\)"
        )
        if not re.search(regex, content):
            self.log(
                f"The file '{self.path}' does not contain a Compiler Explorer badge - trunk version assumed to be missing."
            )
            return False

        return True

    def fix(self):
        self.log(
            "beman-tidy cannot fix this issue. See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#releasegodbolt_trunk_version."
        )
