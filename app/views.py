from django.shortcuts import render
from .models import *
from .forms import *

def home(request):

    if request.method == 'POST':
        form = QuoteForm(request.POST or None)

        if form.is_valid():
            form.save()
    quotes = Quote.objects.all
    context = {'quotes': quotes}
    return render(request, 'home.html', context)

