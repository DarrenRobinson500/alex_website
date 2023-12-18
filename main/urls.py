
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('booking', booking, name='booking'),
    path('quote', quote, name='quote'),
]
