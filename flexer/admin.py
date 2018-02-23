from django.contrib import admin

# Register your models here.
from .models import User, Client, Project, Task
from django.core import urlresolvers

# customized project view in django admin
class ProjectAdmin(admin.ModelAdmin):
    # columns displayed in table
    list_display = ('id', 'name', 'description', 'selected_client', 'show_related_tasks')
    # filter by
    list_filter = ['client']
    # render search field and enable search for datarows with matching values to the search_fields keys
    search_fields = ['id', 'name']

    def selected_client(self, obj):
        # check if project has client assigned
        if hasattr(obj.client, 'id'):
            # create link to the client edit view
            # example url: http://127.0.0.1:8000/admin/flexer/client/16fc865e-e75c-4316-8aa6-8afc47a84445/change/
            link = urlresolvers.reverse("admin:flexer_client_change", args=[obj.client.id])
            # render link to the client with client name as text
            return u'<a href="%s">%s</a>' % (link, obj.client.name)
    # enable <a> element rendering in table
    selected_client.allow_tags=True
    selected_client.short_description = 'client'

    def show_related_tasks(self, obj):
        return u'<a href="/admin/flexer/task/?q=%s">view</a>' % (obj.id)
    show_related_tasks.allow_tags=True
    show_related_tasks.short_description = 'tasks'


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'name', 'task_time', 'view_break_time', 'view_total', 'link_project')
    search_fields = ['project_id__id', 'name']

    def task_time(self, obj):
        start_time = obj.start.strftime("%H:%M")
        end_time = obj.end.strftime("%H:%M")
        return "%s - %s" % (start_time, end_time)
    
    def view_break_time(self, obj):
        return obj.break_time.strftime("%H:%M")
    view_break_time.short_description = 'break'

    def view_total(self, obj):
        return obj.total_hours.strftime("%H:%M")
    view_total.short_description = 'total'

    def link_project(self, obj):
        if hasattr(obj.project_id, 'id'):
            link = urlresolvers.reverse("admin:flexer_project_change", args=[obj.project_id.id])
            return u'<a href="%s">%s</a>' % (link, obj.project_id.name)
    link_project.allow_tags=True
    link_project.short_description = 'project'


class ClientAdmin(admin.ModelAdmin):
    site_title = 'derp derp'
    # change_list_template = 'admin:/templates/flexer/task_admin.html'

admin.site.register(User)
admin.site.register(Task, TaskAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin) # register the extended view