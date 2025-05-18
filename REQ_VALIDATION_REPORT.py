"""
Prints a REQ-by-REQ table showing implementation and test coverage.
"""

# REQ-INF-007
# REQ-INF-010

import re
import os

# Load all declared REQs
# REQ-INF-010
with open("docs/requirements.md") as f:
    req_ids = re.findall(r"REQ-(?:\d+|INF-\d+)", f.read())

# Search for REQ-IDs in a folder (recursively)
# REQ-INF-010
def find_reqs_in(folder, extensions=(".py", ".yml", ".yaml", ".md")):
    found = set()
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extensions):
                try:
                    with open(os.path.join(root, file), errors="ignore") as f:
                        found |= set(re.findall(r"REQ-(?:\d+|INF-\d+)", f.read()))
                except Exception:
                    continue
    return found

# Aggregate all implementation locations
impl = (
    find_reqs_in("src") |
    find_reqs_in(".github") |
    find_reqs_in(".")  # includes root-level enforcement scripts
)

# Search only test files for test coverage
tests = find_reqs_in("tests")

# Generate the coverage table
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
