from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
import os

from twilio.rest import Client

def read_file(text):
    file = open("SECRET_KEYS.txt")
    data = file.readlines()
    file.close()
    for line in data:
        parts = line.strip().split(" ")
        if parts[0] == text:
            return parts[1]


account_sid = read_file("account_sid")
auth_token = read_file("auth_token")
my_twilio_number = read_file("my_twilio_number")
target_number = read_file("target_number")




client = Client(account_sid, auth_token)


def home(request):
    quotes = Quote.objects.order_by('-date')
    videos = Video.objects.all()
    context = {'quotes': quotes, 'videos': videos, }
    return render(request, 'home.html', context)

def videos(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'videos.html', context)

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
        for to in [target_number, ]:
            client.messages.create(body=body, from_=my_twilio_number, to=to)

    return redirect("home")

