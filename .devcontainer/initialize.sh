#!/bin/sh
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

echo "Environment setup complete!"