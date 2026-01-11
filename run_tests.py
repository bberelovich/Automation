import pytest
import sys

if __name__ == "__main__":
    # Remove the script name from the arguments
    args = sys.argv[1:]
    sys.exit(pytest.main(args))
