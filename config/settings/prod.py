# config/settings/prod.py

from .base import *  # noqa: F401, F403
import os
from config.utils import get_database_config_variables

DEBUG = False
ALLOWED_HOSTS = ["flynnt-knapp-8e0b83ab9b88.herokuapp.com"]

database_config_variables = get_database_config_variables(os.getenv("DATABASE_URL"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": database_config_variables["DATABASE_NAME"],
        "HOST": database_config_variables["DATABASE_HOST"],
        "PORT": database_config_variables["DATABASE_PORT"],
        "USER": database_config_variables["DATABASE_USER"],
        "PASSWORD": database_config_variables["DATABASE_PASSWORD"],
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa: F405

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"ACL": "public-read", "CacheControl": "max-age=86400"}
AWS_MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
