#!/bin/sh
set -e

# Install system dependencies
apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    python3-dev \
    git \
    cmake \
    make \
    g++ \
    ninja-build && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

echo "Dependencies Installation Complete"