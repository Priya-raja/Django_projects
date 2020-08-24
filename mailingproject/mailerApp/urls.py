from django.contrib import admin
from django.urls import path, include
from .views import dashboard, register, new_mail, add_new_mail, delete_new_mail, send, save_draft, delete_draft,\
    add_draft

urlpatterns = [
    path('', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('dashboard/', dashboard, name="dashboard"),
    path('delete_draft/', delete_draft, name="delete_draft"),

    path('new_mail/', new_mail, name="subscriber"),
    path('add_new_mail/', add_new_mail, name="add_new_mail"),
    path('delete_new_mail/<int:mail_id>/', delete_new_mail, name="delete_new_mail"),
    path('send/', send, name="send"),
    path('save_draft/', save_draft, name="save_draft"),
    path('add_draft/', add_draft, name="add_draft"),

    path('register/', register, name="register"),




]