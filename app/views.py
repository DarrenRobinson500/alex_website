from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail

from twilio.rest import Client

account_sid = 'ACa0c8a968a5cf31589723fc546a495ca0'
auth_token = '7c2f462ef25881f44a9acecaf8143a80'
my_twilio_number = '19282884569'
daz = '+61493461541'
alex = '+61491062546'

client = Client(account_sid, auth_token)


def home(request):

    quotes = Quote.objects.all
    context = {'quotes': quotes}
    return render(request, 'home.html', context)

def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST or None)
        if form.is_valid(): form.save()

    return redirect("home")

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST or None)
        if form.is_valid(): form.save()
        booking_name = request.POST['name']
        booking_email = request.POST['email']
        booking_subject = request.POST['subject']
        booking_message = request.POST['message']

        body = f"'{booking_name}' has requested a booking",
        for to in [daz, alex]:
            client.messages.create(body=body, from_=my_twilio_number, to=to)

    return redirect("home")

