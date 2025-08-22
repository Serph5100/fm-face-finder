#!/bin/sh
# filepath: /workspaces/fm-face-finder/.devcontainer/initialize.sh
set -e

echo "Setting up Python environment..."

# Install Python packages without pipe-related issues
pip_package_installed() {
  pip list 2>/dev/null | grep -q "^$1[[:space:]]"
}

# Install packages
echo "Checking and installing Python packages..."
pip_package_installed "bing-image-downloader" || pip install bing-image-downloader==1.1.2
pip_package_installed "jupyter" || pip install jupyter==1.1.1

# Set HOME explicitly for pip installations
export HOME="/root"

# Install DeepImageSearch with specific dependencies to avoid conflicts
# Using the PyTorch-based version with compatible torch version
if ! pip_package_installed "DeepImageSearch"; then
  echo "Installing DeepImageSearch and dependencies..."
  pip install torch==2.2.0+cpu --index-url https://download.pytorch.org/whl/cpu
  # Add torchvision with compatible version
  pip install torchvision --index-url https://download.pytorch.org/whl/cpu
  pip install numpy 
  pip install DeepImageSearch==2.5
fi

# Make sure pip binaries are in PATH
export PATH="$PATH:/usr/local/lib/python3.12/site-packages/bin"

echo "Environment setup complete!"