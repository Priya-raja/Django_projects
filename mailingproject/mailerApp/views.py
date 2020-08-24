from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import  render
from .models import Subscriber, Newsletter
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError



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

def save_draft(request):
    messages = Newsletter.objects.all()
    return render(request, 'mailerApp/newsletter.html', {'messages': messages})

def add_draft(request):
    receiver = Newsletter(email=request.POST.get('email', False))
    receiver.save()
    subject = Newsletter(subject=request.POST.get('subject', False))
    subject.save()
    html_content = Newsletter(contents=request.POST.get('contents', False))
    html_content.save()
    draft_mail = [subject, html_content, settings.FROM_EMAIL, [receiver]]

    return render(request, 'mailerApp/draft_mail.html')



@require_POST
def send(request):
    receiver = Newsletter(email=request.POST.get('email', False))
    subject = Newsletter(subject=request.POST.get('subject', False))
    from_email = settings.FROM_EMAIL,
    to = receiver,
    html_content = Newsletter(contents=request.POST.get('contents', False))
    html_content.save()
    if subject and html_content and from_email:
        try:
            send_mail(subject, html_content, from_email, [to], fail_silently=False, )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'mailerApp/newsletter.html', {'receiver': receiver, 'action': send})
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponseRedirect('/add_draft/')

def delete_draft(request):
    mail_delete = Newsletter.objects.all()
    mail_delete.delete()
    return HttpResponseRedirect('/save_draft/')





















