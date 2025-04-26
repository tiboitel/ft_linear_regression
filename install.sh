#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_ROOT/.venv"
REQUIREMENTS_FILE="$PROJECT_ROOT/requirements.txt"
PYTHON=${PYTHON:-python3}

echo "📦 Setting up 'ft_linear_regression'..."

# Check if Python 3 is installed
if ! command -v "$PYTHON" &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ and retry."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "🐍 Creating virtual environment in $VENV_DIR..."
    "$PYTHON" -m venv "$VENV_DIR"
else
    echo "✅ Virtual environment already exists."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Upgrade pip and install requirements
echo "⬆️ Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

# Validate expected files
REQUIRED_FILES=(
    "$PROJECT_ROOT/data/data.csv"
    "$PROJECT_ROOT/src/config.py"
)

echo "🔍 Validating required files..."
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Required file missing: $file"
        exit 1
    fi
done

MODELS_DIRECTORY="/models"

if [ ! -d "$MODELS_DIRECTORY"]; then
    mkdir $MODELS_DIRECTORY; fi

echo "✅ All required files found."

# Optional: Pre-compile Python files to check syntax
echo "🧪 Validating Python syntax..."
python -m compileall "$PROJECT_ROOT/src" "$PROJECT_ROOT/train.py" "$PROJECT_ROOT/predict.py" "$PROJECT_ROOT/plot.py" > /dev/null

# Success message
echo "🎉 Setup complete. Activate your virtual environment with:"
echo ""
echo "    source $VENV_DIR/bin/activate"
echo ""
echo "Then run:"
echo "    python train.py     # To train the model"
echo "    python predict.py   # To make predictions"
echo "    python plot.py      # To visualize the model"

