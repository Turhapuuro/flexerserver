from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=40, blank=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return '%s, %s, %s' % (self.email, self.first_name, self.last_name)

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # Expected format HH:mm
    break_time = models.TimeField(auto_now=False, auto_now_add=False)
    total_hours = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return '%s' % (self.name)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('created',)