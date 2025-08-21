FROM python:3.12-alpine

# Install system dependencies once during image build
RUN apk add --no-cache gcc musl-dev linux-headers python3-dev git

# Set working directory
WORKDIR /workspace

# Keep container running
CMD ["tail", "-f", "/dev/null"]