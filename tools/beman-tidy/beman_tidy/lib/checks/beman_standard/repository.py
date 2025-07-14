#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from ..base.file_base_check import FileBaseCheck
from ..base.base_check import BaseCheck
from ..system.registry import register_beman_standard_check

# [REPOSITORY.*] checks category.
# All checks in this file extend the FileBaseCheck class.
#
# Note: FileBaseCheck is not a registered check!


# TODO REPOSITORY.NAME


@register_beman_standard_check("REPOSITORY.CODEOWNERS")
class RepositoryCodeownersCheck(FileBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config, ".github/CODEOWNERS")

    def check(self):
        # Since this class simply checks for the existence of a CODEOWNERS file,
        # there's nothing more to do than the default pre-check.
        return super().pre_check()

    def fix(self):
        self.log(
            "Please add a CODEOWNERS file to the repository. See https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#repositorycodeowners for more information."
        )


@register_beman_standard_check("REPOSITORY.DEFAULT_BRANCH")
class RepositoryDefaultBranchCheck(BaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        if self.repo_info["default_branch"] == "main":
            return True

        self.log(
            f"The default branch of the repository should be 'main', but it is '{self.repo_info['default_branch']}'."
        )
        return False

    def fix(self):
        self.log(
            "Please change the default branch to 'main'. This typically needs to be done through your Git hosting platform (GitHub, GitLab, etc.)."
        )


# TODO REPOSITORY.DISALLOW_GIT_SUBMODULES
