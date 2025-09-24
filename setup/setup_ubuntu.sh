#!/bin/bash

# Run this script on bash using `bash setup_ubuntu.sh` `./setup_ubuntu.sh`

set -e  # Exit if a command fails

# 0. Check for virtual environment if it doesn't exist
ENV_DIR=".venv"
if [ ! -d "$ENV_DIR" ]; then
    echo "Create a python environment first."
    exit 1
fi

# 1. Activate virtual environment
echo "Activating virtual environment..."
source $ENV_DIR/bin/activate

# 2. Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# 3. Install Python dependencies
echo "Installing Python packages..."
pip install -r requirements.txt

# 4. Start postgres and pgadmin
echo "Starting Docker Compose..."

if ! docker info &> /dev/null; then
    echo "ERROR: Docker daemon is not running."
    exit 1
fi

cd docker 
docker compose up -d