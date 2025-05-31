# accounts/management/commands/createsu.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "Create superuser from env vars"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username=os.getenv("DJANGO_SU_NAME")).exists():
            User.objects.create_superuser(
                username=os.getenv("DJANGO_SU_NAME"),
                email=os.getenv("DJANGO_SU_EMAIL"),
                password=os.getenv("DJANGO_SU_PASSWORD"),
            )
            self.stdout.write("Superuser created.")
        else:
            self.stdout.write("Superuser already exists.")
