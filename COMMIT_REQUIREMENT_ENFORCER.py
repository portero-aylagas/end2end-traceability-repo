"""
Ensure the last commit message contains at least one REQ-ID.
Used in CI to block untraceable commits.
"""

import os
import re

message = os.getenv("COMMIT_MSG", "").strip()

if not re.search(r"REQ-(\d+|INF-\d+)", message):
    print(f"ERROR: Commit message must reference a REQ-ID (e.g., REQ-001 or REQ-INF-000). Found: {message}")
    exit(1)

print(f"✅ Commit message references REQ-ID. OK: {message}")