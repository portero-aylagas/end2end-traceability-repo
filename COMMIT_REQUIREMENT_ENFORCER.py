"""
Ensure the last commit message contains at least one REQ-ID.
Used in CI to block untraceable commits.
"""

import subprocess
import re

def get_latest_non_merge_commit_msg():
    try:
        return subprocess.check_output(
            ["git", "log", "--no-merges", "-1", "--pretty=%B"]
        ).decode("utf-8").strip()
    except Exception as e:
        print("❌ Failed to retrieve commit message:", e)
        exit(1)

commit_message = get_latest_non_merge_commit_msg()

if not re.search(r"REQ-(\d+|INF-\d+)", commit_message):
    print(f"ERROR: Commit message must reference a REQ-ID (e.g., REQ-001). Found: {commit_message}")
    exit(1)

print(f"✅ Commit message references REQ-ID. OK: {commit_message}")
