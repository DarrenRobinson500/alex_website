from django.db import models

class Quote(models.Model):
    quote = models.TextField()
    stars = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now=True, null=True)
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.quote

    def odd(self):
        return self.id % 2 != 0


