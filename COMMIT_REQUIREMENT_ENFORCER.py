"""
Ensure the last commit message contains at least one REQ-ID.
Used in CI to block untraceable commits.
"""

import subprocess
import re

result = subprocess.run(["git", "log", "-1", "--pretty=%B"], stdout=subprocess.PIPE, text=True)
message = result.stdout.strip()

if not re.search(r"REQ-(\d+|INF-\d+)", message):
    print("ERROR: Commit message must reference a REQ-ID (e.g., REQ-001)")
    exit(1)

print("Commit message references REQ-ID. OK.")
