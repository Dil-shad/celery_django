from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = "Hi!celery|TESTING"
        message = "This is a test"
        to_mail = user.email
        print(to_mail)
        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, recipient_list=[to_mail], fail_silently=True)


    return to_mail
