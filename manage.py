#!/usr/bin/env python
# manage.py

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment from .env.dev
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env.dev")


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.dev"),
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
