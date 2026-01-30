#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest

# Capture exit code
EXIT_CODE=$?

# Exit with pytest result
exit $EXIT_CODE