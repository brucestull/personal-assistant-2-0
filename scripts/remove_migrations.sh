#!/bin/bash

# Find all "migrations" directories under apps
find . -type d -name "migrations" | while read -r dir; do
  echo "Cleaning migrations in: $dir"
  find "$dir" -type f ! -name "__init__.py" -delete
done

echo "All migrations (except __init__.py) deleted."
