#!/bin/sh
set -e

# Install system dependencies
apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    git \
    git-lfs \
    cmake \
    make \
    g++ \
    ninja-build && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Initialize git-lfs
git lfs install

pip install --upgrade pip

echo "Dependencies Installation Complete"