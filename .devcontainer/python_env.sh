set -e

echo "Setting up Python environment..."

# Function to check if a Python package is installed
pip_package_installed() {
  pip list 2>/dev/null | grep -q "^$1[[:space:]]"
}

# Install packages
echo "Checking and installing Python packages..."
if ! pip_package_installed "bing-image-downloader"; then
  pip install bing-image-downloader==1.1.2
fi

# Set HOME explicitly for pip installations
export HOME="/root"

# Install DeepImageSearch with specific dependencies to avoid conflicts
# Using the PyTorch-based version with compatible torch version
if ! pip_package_installed "DeepImageSearch"; then
  echo "Installing DeepImageSearch and dependencies..."
  pip install torch==2.2.0+cpu --index-url https://download.pytorch.org/whl/cpu
  pip install torchvision --index-url https://download.pytorch.org/whl/cpu
  pip install numpy
  pip install DeepImageSearch==2.5
fi

# Install autocrop package
if ! pip_package_installed "autocrop"; then
  echo "Installing autocrop package..."
  pip install autocrop
fi

# Upgrade pip and install Jupyter
pip install --upgrade pip
pip install --no-cache-dir jupyter==1.1.1 jupyterlab

# Clean up Jupyter-related cache
find /usr/local/lib/python3.12/site-packages -type d \( -name "jupyter*" -o -name "notebook*" \) -exec rm -rf {}/__pycache__ {}/*.dist-info \; && \
rm -rf /root/.cache/pip /tmp/*

# Make sure pip binaries are in PATH
export PATH="$PATH:/usr/local/lib/python3.12/site-packages"

echo "Environment setup complete!"