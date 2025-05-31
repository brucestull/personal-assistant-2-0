# config/celery.py
import os
from pathlib import Path
from dotenv import load_dotenv

# import django
from celery import Celery

# Load environment variables from .env.dev before anything else
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env.dev")

# Set default settings module using env var, fallback to dev
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.dev")
)

from django.conf import settings  # noqa: E402

# ------------------------------------
# Celery should not need this.
# ------------------------------------
# BAD ADVICE:
# This is a bad practice to set the Django settings module in the Celery app.
# This will ensure that all the Django settings are loaded before Celery starts
# processing tasks. It is crucial for tasks that depend on Django models and other
# settings.

# django.setup()
# ------------------------------------

# Create an instance of the Celery class with a name of 'config'.
# https://docs.celeryq.dev/en/stable/reference/celery.html#celery.Celery
app = Celery("config")

# Pull in all Celery-related settings from Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Set utc false to use local time:
app.conf.enable_utc = False

# Set the timezone to use to convert to and from local time:
app.conf.timezone = settings.TIME_ZONE

app.autodiscover_tasks()
