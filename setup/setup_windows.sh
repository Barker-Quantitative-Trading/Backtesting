#!/bin/bash

# Run this script on bash using `bash setup_windows.sh`

set -e  # Exit if a command fails

# 0. Check for virtual environment if it doesn't exist
ENV_DIR=".venv"
if [ ! -d "$ENV_DIR" ]; then
    echo "Create a python environment first."
    exit 1
fi

# 1. Virtual Environment
python=.venv/Scripts/python.exe

# 2. Upgrade pip
echo "Upgrading pip..."
$python -m pip install --upgrade pip

# 3. Install Python dependencies
echo "Installing Python packages..."
$python -m pip install -r requirements.txt

# 4. Start postgres and pgadmin
echo "Starting Docker Compose..."

# Check if Docker daemon is running
if ! docker info &> /dev/null; then
    echo "ERROR: Docker daemon is not running."
    echo "Please open Docker Desktop and wait until it finishes starting."
    exit 1
fi

cd docker
docker compose up -d