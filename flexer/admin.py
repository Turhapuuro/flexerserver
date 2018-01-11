from django.contrib import admin

# Register your models here.
from .models import User, Client, Project, Task

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Client)
admin.site.register(Project)