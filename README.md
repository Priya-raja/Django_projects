# Django_projects
python django propjects
The application aims at adding subscriber email and sending out mails.

To install, you'll want a virtual environment with the following:

1. pip install django sendgrid
2. Create an account twilio sendigrid (https://www.twilio.com/sendgrid/email-api) and create api key for using the settings.py page
3. Replace your SENDGRID_API_KEY
4. Replace your email Id in settings.py where it asks for USER NAME
5. Login with super user in admin panel where u can add subscriber and send mails to all the recipients.
6.Run using  python manage.py runserver
7. in Browser open http://127.0.0.1:8000/new_mail  for adding emails and deleting
8. To send a mail open http://127.0.0.1:8000/send
