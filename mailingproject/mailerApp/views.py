from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm

from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives

from django.http import HttpResponse
import random


# Create your views here.
# Helper Functions
def index(request):
    return render(request, 'mailerApp/subscribe.html')
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def new_contact(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        subject = 'Newsletter Confirmation',
        from_email = settings.FROM_EMAIL,
        to = sub.email,
        html_content = '<p> Thank you </p>'
        msg = EmailMultiAlternatives(subject, html_content, from_email, to)

        response = msg.send()
        render(request, 'mailerApp/subscribe.html', {'email': to, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'mailerApp/subscribe.html', {'form': SubscriberForm()})



def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'index.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'index.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})