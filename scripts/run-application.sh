#!/usr/bin/env bash

VENV_PATH=".venv"

if [ -n "$VIRTUAL_ENV" ]; then
    echo "✅ A virtual environment is already active at: $VIRTUAL_ENV"
else
    ACTIVATE_SCRIPT="$VENV_PATH/bin/activate"

    if [ -f "$ACTIVATE_SCRIPT" ]; then
        echo "🚀 No environment active. Activating now..."
        source "$ACTIVATE_SCRIPT"
        echo "✨ Virtual environment activated: $VIRTUAL_ENV"
    else
        echo "❌ Error: 'activate' script not found at $ACTIVATE_SCRIPT"
        return 1
    fi
fi

echo "🚀 Running application now..."
python3 src/main.py
