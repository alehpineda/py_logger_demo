import os
import sys

# Completes path and avoids Module not found error for tests
sys.path.insert(
    0, os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "../src"
            )
        )
    )
