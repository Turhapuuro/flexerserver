from django.db import models
import uuid
import datetime

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=40, blank=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return '%s, %s, %s' % (self.email, self.first_name, self.last_name)

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True)
    business_id = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return '%s' % (self.name)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    total_hours = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.name)

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    end = models.DateTimeField(auto_now=False, auto_now_add=False)
    break_time = models.TimeField(auto_now=False, auto_now_add=False)
    total_hours = models.TimeField(auto_now=False, auto_now_add=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ('-date',)
