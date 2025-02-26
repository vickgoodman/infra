#  SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

FROM mcr.microsoft.com/devcontainers/cpp:1-ubuntu-24.04

# Latest CMake needed for most of the beman libraries,
# so we need to install via kitware's apt repo
RUN bash <<EOF
    wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | sudo tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null
    echo 'deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ noble main' | sudo tee /etc/apt/sources.list.d/kitware.list >/dev/null
    sudo apt-get update && sudo apt-get install -y cmake
EOF

# Newer gcc/ llvm is needed to avoid ASAN Stalling, which is turned on by default across beman projects.
# See: https://github.com/google/sanitizers/issues/1614
# Minimal vesion: clang-18.1.3, gcc-13.2
ARG gnu_version=14
RUN bash <<EOT
    sudo apt-get remove -y gcc-${gnu_version} g++-${gnu_version}
    sudo apt-get install -y gcc-${gnu_version} g++-${gnu_version}

    sudo rm -f /usr/bin/gcc
    sudo rm -f /usr/bin/g++

    sudo ln -s /usr/bin/gcc-${gnu_version} /usr/bin/gcc
    sudo ln -s /usr/bin/g++-${gnu_version} /usr/bin/g++

    gcc --version
EOT

USER vscode

# Pre-commit is beman library's standard linting tool
RUN sudo apt-get install -y pipx
RUN pipx install pre-commit
ENV PATH="/home/vscode/.local/bin:${PATH}"

ENTRYPOINT ["/usr/bin/bash"]