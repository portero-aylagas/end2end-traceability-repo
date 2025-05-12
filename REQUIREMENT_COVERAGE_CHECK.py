"""
Validates that all requirements listed in requirements.md are traceable to:
- a function in calculator.py
- a corresponding test case
"""

import re

with open("docs/requirements.md") as f:
    requirements = re.findall(r"REQ-\d+", f.read())

with open("src/calculator.py") as f:
    code = f.read()

with open("tests/test_calculator.py") as f:
    tests = f.read()

missing_in_code = [req for req in requirements if req not in code]
missing_in_tests = [req for req in requirements if req not in tests]

if missing_in_code:
    print("Missing in code:", missing_in_code)
if missing_in_tests:
    print("Missing in tests:", missing_in_tests)

if missing_in_code or missing_in_tests:
    exit(1)
