from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *

admin.site.register(Quote)
admin.site.register(Booking)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)

