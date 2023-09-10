from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from django.utils import timezone
# Create your views here.


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    #send_mail_func.delay(args=["", "another@example.com"])
    return HttpResponse("sent to all")


def schedule_mail(request):
    print("schedule email  triggered.")
    # Create or get a CrontabSchedule
    #hour in 24 hour format
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=4, minute=39)

    # Create a unique task name using a timestamp
    task_name = f"schedule_mail_task_{timezone.now().timestamp()}"

    # Create a PeriodicTask
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name=task_name,
        task='send_mail_app.tasks.send_mail_func',  # Change to our actual task path
        # args=json.dumps([[2, 3]]),  # Uncomment and modify if needed
    )
    return HttpResponse("Done")


