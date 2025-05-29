#!/usr/bin/env python3

import re
import subprocess

# Full SHA you're looking for
full_sha = "23f0ee76b2cef66b0d4f64901ceef41fe2473b54"
short_sha = full_sha[:7]

# Read the log file (assume it's named 'gitlog.txt')
with open("git_log_since_20250515.txt", "r") as f:
    lines = f.readlines()

# Regex pattern to match lines with short SHAs
pattern = re.compile(r"^\*?\s*([0-9a-f]{7})\b", re.IGNORECASE)

# Search for the matching short SHA
for line in lines:
    match = pattern.match(line)
    if match:
        if match.group(1) == short_sha:
            print(f"Match found: {line.strip()}")
            full_sha_from_git = subprocess.check_output(
                ["git", "rev-parse", short_sha], text=True
            ).strip()
            print(f"Full SHA from git: {full_sha_from_git}")
            break
else:
    print(f"No match found for short SHA: {short_sha}")
