
source venv/Scripts/activate

pytest --headless


TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "SUCCESS: All system checks passed gloriously!"
    exit 0
else
    echo "ERROR: Test suite encountered an obstacle. Halting deployment."
    exit 1
fi