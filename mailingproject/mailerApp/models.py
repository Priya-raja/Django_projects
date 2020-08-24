# Create your models here.
from django.db import models
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


class Subscriber(models.Model):

    email_field = models.EmailField(max_length=254)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name + self.email_field


class Newsletter(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    contents = models.TextField(max_length=200)

    def __str__(self):
        return self.subject + self.contents + self.email



