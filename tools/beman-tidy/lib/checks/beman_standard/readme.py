#!/usr/bin/python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from ..base.file_base_check import FileBaseCheck
from ...utils.string import *
from ...utils.git import *
from ..system.registry import register_beman_standard_check

# TODO README.TITLE
# TODO README.BADGES
# TODO README.PURPOSE
# TODO README.IMPLEMENTS
# TODO README.LIBRARY_STATUS


class ReadmeBaseCheck(FileBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config, "README.md")


@register_beman_standard_check("README.TITLE")
class ReadmeTitleCheck(ReadmeBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        lines = self.read_lines_strip()
        first_line = lines[0]

        # Match the pattern "# <library_name>[: <short_description>]"
        regex = r"^# (beman\.[a-zA-Z0-9_]+)(: (.*))?$"
        match = re.match(regex, first_line)
        if not match:
            self.log(
                f"The first line of the file '{self.path}' is invalid. It should start with '# <beman.library_name>[: <short_description>]'.")
            return False

        return True

    def fix(self):
        """
        Fix the issue if the Beman Standard is not applied.
        """
        new_title_line = f"# {self.library_name}: TODO Short Description"
        self.replace_line(0, new_title_line)
        return True


@register_beman_standard_check("README.BADGES")
class ReadmeBadgesCheck(ReadmeBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        """
        self.config["values"] contains a fixed set of Bemanba badges.
        """
        readme_content = self.read()

        values = self.config["values"]
        assert len(values) == 4  # The number of library maturity model states

        # Check if at least one of the required badges is present.
        for value in values:
            if re.search(re.escape(value), readme_content):
                return True

        self.log(
            f"The file '{self.path}' does not contain any of the required badges: {values}")
        return False
