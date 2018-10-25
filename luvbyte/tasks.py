# Create your tasks here
from __future__ import absolute_import, unicode_literals
from luvbyte.celery import luvbyte
from celery import shared_task

celery = Celery(__name__)
celery.config_from_object(__name__)
