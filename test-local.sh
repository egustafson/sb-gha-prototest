#!/bin/bash
# Local testing script for development

set -e

echo "=== sb-gha-prototest Local Test Script ==="
echo

# Check if we can import from local protolib
PROTOLIB_PATH="../sb-gha-protolib"

if [ ! -d "$PROTOLIB_PATH" ]; then
    echo "Error: sb-gha-protolib not found at $PROTOLIB_PATH"
    echo "This script expects the protolib repository to be available at ../sb-gha-protolib"
    exit 1
fi

echo "Found sb-gha-protolib at: $PROTOLIB_PATH"
echo

# Run tests with PYTHONPATH set
echo "Running regression tests..."
echo
PYTHONPATH="$PROTOLIB_PATH:$PYTHONPATH" python main.py

echo
echo "=== Test Complete ==="
