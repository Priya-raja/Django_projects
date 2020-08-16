# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives


# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + str(self.confirmed) + ")"


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.TextField()

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")


    def send(self, request):

        subscribers = Subscriber.objects.filter(confirmed=True)

        for sub in subscribers:
            from_email = settings.FROM_EMAIL,
            to = sub.email,
            subject = self.subject,

            html_content = self.contents

            msg = EmailMultiAlternatives(subject, html_content, from_email, to)

            msg.send()
