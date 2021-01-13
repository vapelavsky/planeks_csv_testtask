web: gunicorn fake_generator.wsgi
release: python manage.py migrate
worker: celery -A fake_generator worker