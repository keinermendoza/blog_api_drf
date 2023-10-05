from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

class SendMailTo:
    
    SITE = 'http://localhost:8000/admin/'
    FROM_EMAIL = 'From keiner@example.com'
    WEBSITE_NAME = "Keiner's blog"

    def __init__(self, user_instance):
        self.user = user_instance
        self.subject = None
        self.html_message = None
        self.plain_message = None

    def wellcome_email(self):
        """sends a wellcome message to the current user"""
        context = {
            'username': self.user.username,
            'website': self.WEBSITE_NAME,
            'date' : timezone.now(),
            'url': self.SITE,
        }

        self.subject = "Wellcome to the Keiner's Blog"
        self.html_message = render_to_string('mail/wellcome.html', context)
        self.plain_message = strip_tags(self.html_message)
        self.send()

    def authentication_email(self):
        """sends an email with the url-token authentication for new users"""

        token = RefreshToken.for_user(self.user)

        context = {
            'username': self.user.username,
            'website': self.WEBSITE_NAME,
            'date' : timezone.now(),
            'url': self.SITE + str(token),
        }

        self.subject = "Validate your email on Keiner's Blog"
        self.html_message = render_to_string('mail/authenticate.html', context)
        self.plain_message = strip_tags(self.html_message)
        self.send()

    def send(self):
        """sends an email using the current values of the Mail class and instance"""
        message = EmailMessage(self.subject, self.html_message, self.FROM_EMAIL, [self.user.email])
        message.content_subtype = 'html' # this is required because there is no plain text email message
        message.send()

