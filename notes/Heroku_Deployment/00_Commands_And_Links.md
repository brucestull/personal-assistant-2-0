# Commands and Links

Run app (loads .env.dev)
- `python manage.py runserver`

Run Celery worker
- `celery -A config worker -l info`

Run Django shell
- `python manage.py shell`

Run DB migrations
- `python manage.py migrate`

Create superuser using env vars
- `python manage.py createsu`
