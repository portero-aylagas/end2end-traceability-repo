# REQ-INF-002
# REQ-INF-008
# REQ-INF-009

import re
import sys
import os

# REQ-INF-009
def is_commit_message_valid(msg):
    match = re.search(r"(REQ-(\d+|INF-\d+))", msg)
    if not match:
        return False
    req_id = match.group(1)
    try:
        with open("docs/requirements.md") as f:
            return req_id in f.read()
    except FileNotFoundError:
        return False

# REQ-INF-002
if __name__ == "__main__":
    commit_message = os.getenv("COMMIT_MSG", "")
    if "Merge" in commit_message:
        sys.exit(0)

    if not is_commit_message_valid(commit_message):
        print(f"ERROR: Commit message must reference a REQ-ID (e.g., REQ-001). Found: {commit_message}")
        sys.exit(1)

    print(f"✅ Commit message is valid and references {commit_message}")
