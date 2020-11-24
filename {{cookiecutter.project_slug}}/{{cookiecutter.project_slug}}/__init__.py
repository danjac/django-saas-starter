from {{ cookiecutter.project_slug }}.config.celery_app import app as celery_app

__all__ = ["celery_app"]
