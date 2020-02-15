from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template

from .forms  import ContactForm
from .models import Restaurant, Restaurant_Foods
from .utils  import SendSubscribeMail

# Currently redirect to ubc area
def redirect_view(request):
    response = redirect("/ubc/")
    return response

# Home view for the given area
def home(request, area):
    restaurant_list = Restaurant.objects.filter(area=area)
    context = {
        'restaurant_list': restaurant_list
    }
    return render(request, 'restaurants/home.html', context)

def map(request, area):
    return render(request, 'restaurants/map.html')

# Render about view
def about(request):
    return render(request, 'restaurants/about.html')

# Contact view
# Render template if provided through GET request
# Attempts to send contact information email if provided through POST request
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name       = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            subject    = form.cleaned_data['subject']
            message    = form.cleaned_data['message']

            # Body of email message template
            template = get_template('restaurants/contact_template.txt')
            context = {
                'contact_email': from_email,
                'form_content': message
            }
            content = template.render(context)

            subject_email = "%s - %s" % (name, subject)

            try:
                # TODO check for possible header injection?
                email = EmailMessage(
                    subject_email,
                    content,
                    'campus.nutrition.ubc@gmail.com',
                    ['campus.nutrition.ubc@gmail.com'],
                    headers = {'Reply-To': from_email},
                )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, 'restaurants/contact.html', {'form': form})

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
    return render(request, 'restaurants/food.html', context)
