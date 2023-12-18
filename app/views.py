from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail

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

        # send_mail(booking_subject + ' ' + booking_name, booking_message, booking_email, ['darrenandamanda.robinson@gmail.com', ])


    return redirect("home")

