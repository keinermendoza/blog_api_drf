from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone

class MailSender:
    
    SITE = 'http://localhost:8000/admin/'
    FROM_EMAIL = 'From keiner@example.com'
            
    @classmethod
    def wellcome(cls, user_data):
        context = {
            'username': user_data['username'],
            'date' : timezone.now(),
            'url': SITE,
        }

        subject = "Wellcome to the Keiner's Blog"
        html_message = render_to_string('mail/wellcome.html', context)
        plain_message = strip_tags(html_message)
        to = 'keiner@example.com'

        # to = user_data['to']
        mail.send_mail(subject, plain_message, cls.FROM_EMAIL, [to], html_message)
