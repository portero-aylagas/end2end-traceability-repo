# REQ-INF-007
# REQ-INF-010
# REQ-INF-011

"""
Prints a REQ-by-REQ table showing implementation and test coverage.

CI will:
- ✅ Allow REQs that are defined but not implemented/tested yet.
- ❌ Block REQs that are implemented but not tested.
- ❌ Block REQ-IDs in code/tests that are not in requirements.md.
"""

import re
import os
import sys

with open("docs/requirements.md") as f:
    req_ids = re.findall(r"REQ-(?:\d+|INF-\d+)", f.read())
    known_reqs = set(req_ids)

def find_reqs_in(folder):
    found = set()
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith((".py", ".yml", ".md")):
                with open(os.path.join(root, file), errors="ignore") as f:
                    found |= set(re.findall(r"REQ-(?:\d+|INF-\d+)", f.read()))
    return found

impl_reqs = (
    find_reqs_in("src")
    | find_reqs_in(".github")
    | find_reqs_in(".")
)
test_reqs = find_reqs_in("tests")

# Detect unknown REQs used in code/tests
unknown_reqs = (impl_reqs | test_reqs) - known_reqs
if unknown_reqs:
    print("❌ ERROR: The following REQ-IDs are used but not declared in requirements.md:")
    for r in sorted(unknown_reqs):
        print(" -", r)
    sys.exit(1)

# Table output
print("| REQ ID       | Implemented | Tested |")
print("|--------------|-------------|--------|")
fail = False
for req in sorted(known_reqs):
    impl = "✅" if req in impl_reqs else "❌"
    test = "✅" if req in test_reqs else "❌"
    print(f"| {req:<12} |     {impl}     |   {test}  |")
    if impl == "✅" and test == "❌":
        fail = True  # implemented but not tested → BLOCK

print()
if fail:
    print("❌ One or more implemented REQs are missing tests.")
    sys.exit(1)
else:
    print("✅ REQ enforcement passed.")
