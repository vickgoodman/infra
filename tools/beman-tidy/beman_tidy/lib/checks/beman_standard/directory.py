#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import os
from ..base.directory_base_check import DirectoryBaseCheck
from ..system.registry import register_beman_standard_check


# [DIRECTORY.*] checks category.
class BemanTreeDirectoryCheck(DirectoryBaseCheck):
    """
    Check if the directory tree is a Beman tree.
    """

    def __init__(self, repo_info, beman_standard_check_config, prefix_path):
        super().__init__(
            repo_info,
            beman_standard_check_config,
            f"{prefix_path}/beman/{repo_info['name']}",
        )


@register_beman_standard_check("DIRECTORY.INTERFACE_HEADERS")
class DirectoryInterfaceHeadersCheck(DirectoryBaseCheck):
    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config, ".")

    def check(self):
        """
        Check that all public header files reside within the include/beman/<short_name>/ directory.
        """
        # Check if the path exists.
        # Example path: "exemplar/include/beman/exemplar"
        include_path = self.path / "include" / "beman" / self.repo_info["name"]
        if (
            not os.path.exists(include_path)
            or os.path.isfile(include_path)
            or len(os.listdir(include_path)) == 0
        ):
            self.log(
                f"The path '{self.path}' does not exist, is a file or is empty."
                " All public header files must reside within include/beman/<short_name>/."
            )
            return False

        # Get all .hpp files paths, excluding certain directories.
        exclude_dirs = {"src"}
        if self.repo_info["name"] == "exemplar":
            exclude_dirs.add("cookiecutter")

        hpp_files = []
        for root, dirs, files in os.walk(self.path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for name in files:
                if name.lower().endswith(".hpp"):
                    hpp_files.append(os.path.join(root, name))

        # Check that all .hpp files are under the include/beman/<short_name>/
        for hpp_file in hpp_files:
            if not hpp_file.startswith(str(include_path)):
                self.log(
                    f"Header file '{hpp_file}' is not under include/beman/{self.repo_info['name']}/ directory."
                    " All public header files must reside within include/beman/<short_name>/."
                )
                return False

        return True

    def fix(self):
        pass


# TODO DIRECTORY.IMPLEMENTATION_HEADERS


# TODO DIRECTORY.SOURCES
@register_beman_standard_check("DIRECTORY.SOURCES")
class DirectorySourcesCheck(BemanTreeDirectoryCheck):
    """
    Check if the sources directory is src/beman/<short_name>.
    """

    def __init__(self, repo_info, beman_standard_check_config):
        super().__init__(repo_info, beman_standard_check_config, "src")

    def check(self):
        return self.pre_check()

    def fix(self):
        """
        TODO: Implement the fix.
        """
        pass


# TODO DIRECTORY.TESTS


# TODO DIRECTORY.EXAMPLES


# TODO DIRECTORY.DOCS


# TODO DIRECTORY.PAPERS
