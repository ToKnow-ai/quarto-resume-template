#!/bin/bash

# Name of the virtual environment
VENV_NAME=".resume_env"

# Check if the virtual environment already exists
if [ -d "$VENV_NAME" ]; then
    echo "Virtual environment $VENV_NAME already exists. Activating..."
    source "$VENV_NAME/bin/activate"
else
    echo "Creating new virtual environment $VENV_NAME..."
    python3 -m venv "$VENV_NAME"
    source "$VENV_NAME/bin/activate"
fi

# Check if the activation was successful
if [ $? -eq 0 ]; then
    echo "Virtual environment activated successfully."
else
    echo "Failed to activate virtual environment. Exiting."
    exit 1
fi

# Install or upgrade pip
pip install --upgrade pip

# Install packages from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing packages from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping package installation."
fi

echo "Environment setup complete. You can now run your Python scripts."