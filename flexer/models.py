from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=40, blank=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return '%s, %s, %s' % (self.email, self.first_name, self.last_name)