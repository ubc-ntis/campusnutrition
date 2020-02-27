import threading
import mailchimp
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
from django import utils
from django.http import JsonResponse
from .models import Restaurant

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


def util_render(request, path, context={}):

    # Add context variables common to all views
    context = {
        **context,
        "tracking_id": settings.TRACKING_ID
    }

    return render(request, path, context)
  
  # Get JSON of lat and lon
# TODO add more details later
def getGeoJSON(request, area):
    response = Restaurant.objects.filter(area=area).values('lat','lng', 'address')
    print(response)
    return JsonResponse(list(response), safe=False)