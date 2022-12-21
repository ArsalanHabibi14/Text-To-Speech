from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "text_to_audio.settings")
app = Celery("text_to_audio")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
