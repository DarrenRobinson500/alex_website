from django.forms import *
from .models import *

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields= ['quote', 'name', 'stars']

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields= ['name', 'subject', 'email', 'message', ]

