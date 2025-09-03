set -e

echo "Setting up Python environment..."

# Function to check if a Python package is installed
pip_package_installed() {
  pip list 2>/dev/null | grep -q "^$1[[:space:]]"
}

# Ensure pip binaries are in PATH
export PATH="$PATH:/usr/local/lib/python3.12/site-packages"
export HOME="/root"

# Install Python packages
echo "Checking and installing required Python packages..."

# Install better-bing-image-downloader
if ! pip_package_installed "better-bing-image-downloader"; then
  echo "Installing better-bing-image-downloader..."
  pip install better-bing-image-downloader==2.0
fi

if ! pip_package_installed "head_detector"; then
  echo "Installing head_detector..."
  pip install torchvision==0.15.2+cpu --index-url https://download.pytorch.org/whl/cpu
  pip install git+https://github.com/KupynOrest/head_detector.git
fi

# Install DeepImageSearch and its dependencies
if ! pip_package_installed "DeepImageSearch"; then
  echo "Installing DeepImageSearch and its dependencies..."
  pip install faiss-cpu==1.7.3
  pip install DeepImageSearch==2.5
fi

# Install autocrop
if ! pip_package_installed "autocrop"; then
  echo "Installing autocrop..."
  pip install autocrop
fi

# Install scikit-image
if ! pip_package_installed "scikit-image"; then
  echo "Installing scikit-image..."
  pip install scikit-image
fi

# Reinstall Jupyter to ensure binaries are created in /usr/local/bin
echo "Reinstalling Jupyter to ensure binaries are linked..."
pip install --no-cache-dir --force-reinstall jupyter

# Downgrading Numpy to 1.26.4 for compatibility between packages.
pip install --force-reinstall numpy==1.26.4

echo "Python environment setup complete!"