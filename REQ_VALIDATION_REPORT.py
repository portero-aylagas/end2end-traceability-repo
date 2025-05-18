# REQ-INF-007
# REQ-INF-010
# REQ-INF-011

"""
Prints a REQ-by-REQ table showing implementation and test coverage.

CI fails if any REQ is implemented (in code) but not tested.
Unimplemented REQs are allowed (to support forward planning).
"""

import os
import re

with open("docs/requirements.md") as f:
    req_ids = re.findall(r"REQ-(?:\d+|INF-\d+)", f.read())

def find_reqs_in(folder):
    found = set()
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith((".py", ".yml", ".md")):
                with open(os.path.join(root, file), errors="ignore") as f:
                    found |= set(re.findall(r"REQ-(?:\d+|INF-\d+)", f.read()))
    return found

impl = (
    find_reqs_in("src") |
    find_reqs_in(".github") |
    find_reqs_in(".")  # for top-level CI scripts
)
tests = find_reqs_in("tests")

print("| REQ ID       | Implemented | Tested |")
print("|--------------|-------------|--------|")
failed = False
for req in sorted(req_ids):
    is_impl = req in impl
    is_test = req in tests
    imp = "✅" if is_impl else "❌"
    tst = "✅" if is_test else "❌"

    if is_impl and not is_test:
        failed = True  # only fail if implemented but not tested

    print(f"| {req:<12} |     {imp}     |   {tst}  |")

print()
if failed:
    print("❌ One or more REQs are implemented but not tested.")
    exit(1)
else:
    print("✅ All implemented REQs are properly tested.")
