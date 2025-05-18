"""
Automatically generates TRACEABILITY.md from requirements, code, and tests.
"""
# REQ-INF-012

import re

with open("SPECIFICATION.md") as f:
    specs = re.findall(r"SPEC-\d+", f.read())

with open("docs/requirements.md") as f:
    req_map = re.findall(r"(REQ-\d+).*?(SPEC(?:-NF)?-\d+)", f.read())

with open("src/calculator.py") as f:
    code = f.read()

with open("tests/test_calculator.py") as f:
    tests = f.read()

rows = []
for req, spec in req_map:
    code_ref = f"src/calculator.py::{req}" if req in code else "❌"
    test_ref = f"tests/test_calculator.py::{req}" if req in tests else "❌"
    rows.append((spec, req, code_ref, test_ref))

with open("TRACEABILITY.md", "w") as f:
    f.write("# Traceability Matrix\n\n")
    f.write("| Spec ID  | Req ID  | Code Module             | Test Case                       |\n")
    f.write("|----------|---------|--------------------------|----------------------------------|\n")
    for row in rows:
        f.write(f"| {' | '.join(row)} |\n")

print("TRACEABILITY.md generated.")
