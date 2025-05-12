"""
Detects tests for unknown or undeclared requirements.
"""

import re

with open("tests/test_calculator.py") as f:
    tests = f.read()

reqs_in_tests = set(re.findall(r"REQ-\d+", tests))

with open("docs/requirements.md") as f:
    declared_reqs = set(re.findall(r"REQ-\d+", f.read()))

unknown_tests = reqs_in_tests - declared_reqs
if unknown_tests:
    print("Tests refer to undeclared requirements:", unknown_tests)
    exit(1)
