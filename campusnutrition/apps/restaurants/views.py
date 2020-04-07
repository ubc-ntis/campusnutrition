from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.conf import settings

from .utils import getGeoJSON
from .forms  import ContactForm
from .models import Restaurant, Restaurant_Foods
from .utils  import SendSubscribeMail, send_contact_email, util_render
from .filters import RestaurantFilter

# Currently redirect to ubc area
def redirect_view(request):
    response = redirect("/ubc/")
    return response

# Home view for the given area
def home(request, area):
    restaurant_list = Restaurant.objects.filter(area=area)
    restaurant_list_filter = RestaurantFilter(request.GET, queryset=restaurant_list) 
    context = {
        'restaurant_list': restaurant_list_filter
    }
    return util_render(request, 'restaurants/home.html', context)

def map(request, area):
    return util_render(request, 'restaurants/map.html')

# Render about view
def about(request):
    return util_render(request, 'restaurants/about.html')

# Contact view
# Render template if provided through GET request
# Attempts to send contact information email if provided through POST request
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():

            name          = form.cleaned_data['name']
            from_email    = form.cleaned_data['from_email']
            subject       = form.cleaned_data['subject']
            message       = form.cleaned_data['message']

            subject_email_campus  = "Contact Form Submission: %s - %s" % (name, subject)
            subject_email_confirm = "Thank you for your submission"

            status = send_contact_email(subject_email_campus,
                                        message,
                                        "restaurants/contact_campus.txt",
                                        settings.CONTACT_EMAIL_ADDRESS,
                                        [settings.CONTACT_EMAIL_ADDRESS],
                                        headers = {
                                            "Reply-To": from_email
                                        })

            status &= send_contact_email(subject_email_confirm,
                                         message,
                                         "restaurants/contact_confirm.txt",
                                         settings.CONTACT_EMAIL_ADDRESS,
                                         [from_email])

            if status == False:
                return HttpResponse("Invalid header found")

    return util_render(request, 'restaurants/contact.html', {'form': form})

# Subscribe view
def subscribe(request):
    if request.method == "POST":
        email = request.POST["email_id"]

        send_sub_mail = SendSubscribeMail(email)

        # Send the email
        # Status is True when subscription is successful,
        # False when unsuccessful (email already added to Mailchimp)
        status = send_sub_mail.run()

        if status:
            # Subscription successful 
            return HttpResponse("/")
        else:
            # Subscription failed
            data = {"status": "404"}
            return JsonResponse(data)

def food(request, area, name):
    Restaurant_food_list = Restaurant_Foods.objects.filter(area=area).filter(name=name)
    context = {
        'restaurant_food_list': Restaurant_food_list
    }
    return util_render(request, 'restaurants/food.html', context)
