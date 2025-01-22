#!/usr/bin/python3
# SPDX-License-Identifier: 2.0 license with LLVM exceptions

from .run import run_command
import os
import sys

from git import Repo, InvalidGitRepositoryError


def get_repo_info(path):
    """
    Get information about the Git repository at the given path.
    Returns a dictionary with data about the repository.
    """

    try:
        # Initialize the repository object
        repo = Repo(os.path.abspath(path), search_parent_directories=True)

        # Get the top-level directory of the repository
        top_level_dir = repo.git.rev_parse("--show-toplevel")

        # Get the repository name (directory name of the top level)
        repo_name = os.path.basename(top_level_dir)

        # Get the remote URL (assuming 'origin' is the remote name)
        remote_url = None
        if "origin" in repo.remotes:
            remote_url = repo.remotes.origin.url

        # Get the current branch
        current_branch = repo.active_branch.name

        # Get the commit hash
        commit_hash = repo.head.commit.hexsha

        # Get the status of the repository
        status = repo.git.status()

        # Get unstaged changes
        unstaged_changes = repo.git.diff("--stat")

        return {
            "top_level": top_level_dir,
            "name": repo_name,
            "remote_url": remote_url,
            "current_branch": current_branch,
            "commit_hash": commit_hash,
            "status": status,
            "unstaged_changes": unstaged_changes,
        }
    except InvalidGitRepositoryError:
        print(f"The path '{path}' is not inside a valid Git repository.")
        sys.exit(1)
    except Exception as e:
        print(
            f"An error occurred while getting repository information. Check {path}.")
        sys.exit(1)
