from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def new_contact(request):
    if request.method == 'POST':
        receiver = User(email=request.POST['email'])
        receiver.save()
        subject = 'Newsletter Confirmation',
        from_email = settings.FROM_EMAIL,
        to = receiver.email,
        html_content = '<p> Thank you </p>'
        msg = EmailMultiAlternatives(subject, html_content, from_email, to)

        response = msg.send()
        render(request, 'mailerApp/subscribe.html', {'email': to, 'action': 'added', 'form': CustomUserCreationForm})
    else:
        return render(request, 'mailerApp/subscribe.html', {'form': CustomUserCreationForm})



