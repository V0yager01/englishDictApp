from celery import shared_task

from django.core.mail import send_mail

from englishDictApp.settings import EMAIL_HOST_USER

SUBJECT = 'Account verification'

@shared_task
def email_verification(link, recipient_list):
    send_mail(
        SUBJECT,
        link,
        EMAIL_HOST_USER,
        recipient_list
    )