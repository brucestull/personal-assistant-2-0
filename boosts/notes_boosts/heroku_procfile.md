# Procfile

## Before Celery Installation

```bash
web: gunicorn config.wsgi
release: python manage.py migrate accounts && python manage.py migrate
worker: celery -A config worker --loglevel=info
```

## After Celery Installation

```bash
web: gunicorn config.wsgi
worker: celery -A config worker --loglevel=info
beat: celery -A config beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
