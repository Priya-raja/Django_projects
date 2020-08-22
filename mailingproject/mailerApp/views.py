from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login


from django.shortcuts import get_object_or_404, render
from .models import Subscriber, Newsletter
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm
from django.urls import reverse



from django.core.mail import EmailMultiAlternatives



# Create your views here.
# Helper Functions

def dashboard(request):
    return render(request, "mailerApp/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def new_mail(request):
    all_emails = Subscriber.objects.all()

    return render(request, 'mailerApp/subscriber.html', {'all_emails': all_emails})

def add_new_mail(request):
    receiver = Subscriber(email_field=request.POST.get('email_field', False))
    receiver.save()
    print(receiver)
    return HttpResponseRedirect('/new_mail/')

def delete_new_mail(request, mail_id):
    mail_delete = Subscriber.objects.get(id=mail_id)
    mail_delete.delete()
    return HttpResponseRedirect('/new_mail/')

def send(request):
    send_mail = Newsletter.objects.all()
    if request.method == 'POST':
        receiver = Subscriber(email_field=request.POST.get('email_field', False))
        receiver.save()
        subject = 'Newsletter Confirmation',
        from_email = settings.FROM_EMAIL,
        to = receiver.email_field,
        html_content = '<p> Thank you </p>'
        msg = EmailMultiAlternatives(subject, html_content, from_email, to)

        response = msg.send()
        render(request, 'mailerApp/newsletter.html', {'email': to, 'action': 'added'})
    else:
        return render(request, 'mailerApp/newsletter.html', {'send_mail': send_mail})


















