from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_django.settings")

app = Celery('celery_django')
app.conf.enable_utc = False

app.conf.update(timezone='Aisa/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')


# celery Beat settings
app.conf.beat_schedule = {
    
}

app.autodiscover_task = ()


@app.task(bind=True)
def debug_task(self):
    print(f'Request:{slef.request!r}')


