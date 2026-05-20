#!/bin/bash

# 1. Step inside and activate the project virtual environment
source venv/Scripts/activate

# 2. Execute the automated test suite in headless memory mode
pytest --headless

# 3. Capture the success/failure status code from the test run
TEST_RESULT=$?

# 4. Return exit code 0 if all tests passed, or 1 if something failed
if [ $TEST_RESULT -eq 0 ]; then
    echo "SUCCESS: All system checks passed gloriously!"
    exit 0
else
    echo "ERROR: Test suite encountered an obstacle. Halting deployment."
    exit 1
fi