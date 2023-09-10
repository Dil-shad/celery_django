from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# from django_celery_beat.models import PeriodicTask


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_django.settings")

app = Celery('celery_django')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings', namespace='CELERY')


# celery Beat settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8':{
        'task':'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=3, minute=46) #day_of_month=1,month_of_year=1,
        #'args':(2,)

    } 
}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}') 


