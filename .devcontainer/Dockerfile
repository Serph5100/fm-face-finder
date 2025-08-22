FROM python:3.12-alpine

# Install system dependencies
RUN apk add --no-cache gcc musl-dev linux-headers python3-dev git

# Install Jupyter without caching and remove only Jupyter-related cache
RUN pip install --no-cache-dir jupyter jupyterlab && \
    find /usr/local/lib/python3.12/site-packages -type d \( -name "jupyter*" -o -name "notebook*" \) -exec rm -rf {}/__pycache__ {}/*.dist-info \; && \
    rm -rf /root/.cache/pip /tmp/*

# Set working directory
WORKDIR /workspace

# Keep container running
CMD ["tail", "-f", "/dev/null"]