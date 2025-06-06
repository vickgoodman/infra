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
    """
    Check https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#readmetitle
    """
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        
        lines = self.read_lines_strip()
        if len(lines) == 0:
            return False
        first_line = lines[0]

        # Match the pattern "# <library_name>[: <short_description>]"
        if not first_line[2:].startswith(f"{self.library_name}:"):
            return False

        return True

    def fix(self):
        """
        Fix the issue if the Beman Standard is not applied.
        """
        # TODO: Implement the fix.
        return False


@register_beman_standard_check("README.BADGES")
class ReadmeBadgesCheck(ReadmeBaseCheck):
    """
    Check https://github.com/bemanproject/beman/blob/main/docs/BEMAN_STANDARD.md#readmebadges
    """
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config)

    def check(self):
        """
        Badge format: ![Name with multiple words](url_no_spaces)
        Badge line format: ![Name1](url1) ![Name2](url2) ![Name3](url3) ...
        """
        repo_badges = self.parse_lines(self.read_lines_strip())
        if repo_badges is None:
            self.log(f"First line of README.md must contain badges.")
            return False

        standard_badges = match_badges(self.full_text_body)
        if standard_badges is None:
            self.log(
                f"No badges found in Beman Standard. Please add badge examples to the Beman Standard in section README.BADGES.")
            return False

        # Check if the badges in the README.md are the same as in the Beman Standard.
        for badge_name, badge_url in repo_badges:
            matched_badge = next(
                (standard_badge for standard_badge in standard_badges if standard_badge[0] == badge_name), None)
            if not matched_badge:
                self.log(
                    f"Badge \"{badge_name}\" not found in the Beman Standard. Standard badges: {set([badge[0] for badge in standard_badges])}.")
                return False
            beman_standard_badge_url = matched_badge[1]

            if badge_name == "Library Status":
                if not badge_url.startswith("https://raw.githubusercontent.com/bemanproject/beman/refs/heads/main/images/badges/beman_badge-beman_library_"):
                    self.log(
                        f"Badge \"{badge_name}\" URL is invalid: {badge_url}. The URL should start with \"https://raw.githubusercontent.com/bemanproject/beman/refs/heads/main/images/badges/beman_badge-beman_library_\".")
                    return False

                if badge_url not in [standard_badge[1] for standard_badge in standard_badges]:
                    self.log(
                        f"Badge \"{badge_name}\" URL is invalid: {badge_url}. The URL should be in the Beman Standard.")
                    return False

            if not validate_url(badge_url):
                self.log(
                    f"Badge \"{badge_name}\" URL is invalid: {badge_url}.")
                return False

        return True

    def parse_lines(self, lines):
        if lines is None or len(lines) == 0:
            return None

        lines = skip_lines(lines, 1)    # Skip the title.
        lines = skip_empty_lines(lines)  # Skip empty lines.
        # Skip 3 lines of "SPDX-License-Identifier"
        lines = skip_lines(lines, 3)
        lines = skip_empty_lines(lines)  # Skip empty lines.
        badge_line = lines[0] if len(lines) > 0 else None
        lines = skip_lines(lines, 1)    # Skip the badges.
        if len(lines) > 0:
            # No more badges on remaining lines.
            if any(match_badges(line) for line in lines):
                self.log(f"Only one line of badges is allowed.")
                return None

        return match_badges(badge_line)
