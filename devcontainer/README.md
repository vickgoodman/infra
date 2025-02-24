# Devcontainer

<!-- SPDX-License-Identifier: 2.0 license with LLVM exceptions -->

This folder contains the infrastructure for beman project's 
generic devcontainer image. You can checkout the image in beman's 
[GitHub Packages page](https://github.com/orgs/bemanproject/packages/container/package/devcontainers).

The image is build on top of GitHub's 
[C++ devcontainer image](https://github.com/devcontainers/images/tree/main/src/cpp)
for ubuntu 24.04.

The image includes:

- The latest CMake from kitware's apt repository
- GNU compiler version 14 (this is configurable via docker build arg)

## Building your own image

You can build your own beman devcontainer image with:

```bash
docker build devcontainer/
```