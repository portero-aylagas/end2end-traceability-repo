"""
Validates that each requirement has a corresponding row in TRACEABILITY.md.
"""

import re

with open("docs/requirements.md") as f:
    requirements = set(re.findall(r"REQ-\d+", f.read()))

with open("TRACEABILITY.md") as f:
    trace = f.read()

missing_from_trace = [req for req in requirements if req not in trace]

if missing_from_trace:
    print("Missing from traceability matrix:", missing_from_trace)
    exit(1)

exit(0)
