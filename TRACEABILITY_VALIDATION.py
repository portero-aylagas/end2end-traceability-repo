# REQ-INF-013

import os
import sys

matrix_path = "TRACEABILITY.md"

if not os.path.exists(matrix_path):
    print(f"❌ ERROR: '{matrix_path}' not found.")
    print("➡️  Run GENERATE_TRACEABILITY_MATRIX.py first or check CI pipeline ordering.")
    sys.exit(1)

# Proceed with normal validation logic
with open(matrix_path) as f:
    content = f.read()

# Basic sanity check
if "Traceability Matrix" not in content or "REQ" not in content:
    print("❌ TRACEABILITY.md appears to be malformed.")
    sys.exit(1)

print("✅ TRACEABILITY.md exists and appears to be structured correctly.")
