"""
Detects implementation of code not tied to a requirement.
"""

import re

with open("src/calculator.py") as f:
    code = f.read()

reqs_in_code = set(re.findall(r"REQ-\d+", code))

with open("docs/requirements.md") as f:
    declared_reqs = set(re.findall(r"REQ-\d+", f.read()))

unknown_implementations = reqs_in_code - declared_reqs
if unknown_implementations:
    print("Code implements undeclared requirements:", unknown_implementations)
    exit(1)
