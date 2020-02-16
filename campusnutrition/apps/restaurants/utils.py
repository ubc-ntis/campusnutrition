import threading
import mailchimp
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings

class SendSubscribeMail(object):

    def __init__(self, email):
        self.email = email

    def run(self):
        API_KEY = settings.MAILCHIMP_API_KEY
        LIST_ID = settings.MAILCHIMP_SUBSCRIBE_LIST_ID

        api = mailchimp.Mailchimp(API_KEY)

        try:
            api.lists.subscribe(LIST_ID, {"email": self.email}, 
                                double_optin = False)
            return True
        except:
            return False

def send_contact_email(subject, message, template_file, from_email, to_email_list, headers={}):

    # Body of email message template
    template = get_template(template_file)

    context_campus = {
        'contact_email': from_email,
        'form_content': message
    }

    content = template.render(context_campus)

    display_name = "%s <%s>" % (settings.CONTACT_DISPLAY_NAME, from_email)

    try:

        email = EmailMessage(
            subject,
            content,
            display_name,
            to_email_list,
            headers = headers
        )

        email.send()

        return True

    except:

        return False
