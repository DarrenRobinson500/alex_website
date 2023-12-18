from django.db.models import *

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
