from django.db.models import *

from embed_video.fields import EmbedVideoField

class Video(Model):
    video = EmbedVideoField()  # same like models.URLField()
    name = TextField(null=True, blank=True)
    category = TextField(null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return "No name"

class Quote(Model):
    quote = TextField(null=True, blank=True)
    stars = IntegerField(null=True, blank=True)
    date = DateField(auto_now=True, null=True)
    name = TextField(null=True, blank=True)

    def __str__(self):
        return self.quote

    def odd(self):
        return self.id % 2 != 0

class Booking(Model):
    name = CharField(max_length=255)
    email = EmailField(null=True, blank=True)
    subject = TextField(null=True, blank=True)
    message = TextField(null=True, blank=True)
    date = DateField(auto_now=True, null=True)

    def __str__(self):
        return self.subject
