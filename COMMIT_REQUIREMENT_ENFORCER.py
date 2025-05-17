# REQ-INF-002: Require REQ-ID in commit messages
# REQ-INF-008: Enforce REQ traceability checks in CI
# REQ-INF-009: Validate REQ-ID exists in requirements.md

import re
import os
import sys

# 1. Pull message from environment (CI sets COMMIT_MSG)
commit_message = os.getenv("COMMIT_MSG", "")
if "Merge" in commit_message:
    # Allow merge commits but don't validate them
    sys.exit(0)

# 2. Validate REQ-ID exists syntactically
match = re.search(r"(REQ-(\d+|INF-\d+))", commit_message)
if not match:
    print(f"ERROR: Commit message must reference a REQ-ID (e.g., REQ-001). Found: {commit_message}")
    sys.exit(1)

# 3. Cross-check against requirements.md
req_id = match.group(1)

try:
    with open("docs/requirements.md") as f:
        if req_id not in f.read():
            print(f"ERROR: REQ-ID {req_id} not found in requirements.md")
            sys.exit(1)
except FileNotFoundError:
    print("ERROR: requirements.md not found.")
    sys.exit(1)

# ✅ Valid
print(f"✅ Commit message is valid and references {req_id}")
