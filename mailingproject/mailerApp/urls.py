from django.contrib import admin
from django.urls import path, include
from .views import dashboard, register, new_mail, add_new_mail, delete_new_mail, send

urlpatterns = [
    path('', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('dashboard/', dashboard, name="dashboard"),
    path('new_mail/', new_mail, name="subscriber"),
    path('add_new_mail/', add_new_mail, name="add_new_mail"),
    path('delete_new_mail/<int:mail_id>/', delete_new_mail, name="delete_new_mail"),
    path('send/', send, name="send"),

    path('register/', register, name="register"),




]