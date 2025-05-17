"""
Ensure every function in code/tests explicitly references a REQ-ID.
"""

import os
import re

req_pattern = re.compile(r"REQ-(\d+|INF-\d+)")
def_pattern = re.compile(r"^\s*def\s+\w+\(.*\):")

missing_annotations = []

for root, _, files in os.walk("src"):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file)) as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if def_pattern.match(line):
                        comment_line = lines[i-1] if i > 0 else ""
                        if not req_pattern.search(comment_line):
                            missing_annotations.append(f"{file}:{i+1} {line.strip()}")

for root, _, files in os.walk("tests"):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file)) as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if def_pattern.match(line):
                        comment_line = lines[i-1] if i > 0 else ""
                        if not req_pattern.search(comment_line):
                            missing_annotations.append(f"{file}:{i+1} {line.strip()}")

if missing_annotations:
    print("ERROR: The following functions are missing REQ-ID comments:")
    for entry in missing_annotations:
        print(" -", entry)
    exit(1)

print("All functions and tests are properly annotated with REQ-IDs.")
