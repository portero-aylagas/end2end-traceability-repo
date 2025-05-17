"""
Prints a REQ-by-REQ table showing implementation and test coverage.
"""

# REQ-INF-007
# REQ-INF-010

import re
import os

# REQ-INF-010
with open("docs/requirements.md") as f:
    req_ids = re.findall(r"REQ-(?:\d+|INF-\d+)", f.read())

# REQ-INF-010
def find_reqs_in(folder):
    found = set()
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file)) as f:
                    found |= set(re.findall(r"REQ-(?:\d+|INF-\d+)", f.read()))
    return found

impl = find_reqs_in("src")
tests = find_reqs_in("tests")

print("| REQ ID       | Implemented | Tested |")
print("|--------------|-------------|--------|")
failed = False
for req in sorted(req_ids):
    imp = "✅" if req in impl else "❌"
    tst = "✅" if req in tests else "❌"
    if imp == "❌" or tst == "❌":
        failed = True
    print(f"| {req:<12} |     {imp}     |   {tst}  |")

print()
if failed:
    print("❌ One or more REQs are missing implementation or tests.")
    exit(1)
else:
    print("✅ All REQs are fully implemented and tested.")
