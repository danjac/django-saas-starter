# Standard Library
import os

# Third Party Libraries
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_slug }}.config.settings.local")

app = Celery("{{ cookiecutter.project_slug }}")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request}")
