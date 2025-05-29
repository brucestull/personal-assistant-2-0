#!/bin/bash

# Find all "migrations" directories under apps
find . -type d -name "migrations" | while read -r dir; do
  echo "Checking migrations in: $dir"
  if [ "$(find "$dir" -type f ! -name "__init__.py" | wc -l)" -gt 0 ]; then
    echo "Migrations found in $dir"
  else
    echo "No migrations found in $dir"
  fi
done