from django.contrib import admin
from django.urls import path, include
from .views import dashboard, register,new_contact

urlpatterns = [
    path('', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('dashboard/', dashboard, name="dashboard"),
    path('new_contact/', dashboard, name="new"),
    path('register/', register, name="register"),
    path('new/', new_contact, name='new'),



]