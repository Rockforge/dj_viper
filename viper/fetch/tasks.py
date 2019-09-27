from celery import current_app
from django.conf import settings
import os
import subprocess


@current_app.task(bind=True)
def run_duck_search(self, query):
    params = [
        'python',
        os.path.join(
            settings.SCRIPT_DIR,
            'ducksearch.py',
        ),
        query,
    ]

    subprocess.check_call(params)

