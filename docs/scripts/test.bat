#!/usr/bin/env bash

case "$(uname -s)" in
    Linux*)
        echo "Running on Linux"
        # Linux commands here
        ;;
    Darwin*)
        echo "Running on macOS"
        # macOS commands here (optional)
        ;;
    CYGWIN*|MINGW*|MSYS*)
        echo "Running on Windows"
        # Windows commands here
        ;;
    *)
        echo "Unknown OS: $(uname -s)"
        ;;
esac
