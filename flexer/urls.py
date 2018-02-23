from django.conf.urls import url
from . import views
from flexer import views

urlpatterns = [
    # url(r'', views.index, name='index'),
    url(r'^users/$', views.user_list),
    url(r'^clients/$', views.fetch_clients),
    url(r'^clients/(?P<pk>[^/]+)/$', views.manage_client),
    url(r'^projects/$', views.fetch_projects),
    url(r'^projects/(?P<pk>[^/]+)/$', views.manage_project),
    url(r'^tasks/$', views.fetch_tasks),
    url(r'^tasks/(?P<pk>[^/]+)/$', views.manage_task),  
    url(r'^overview/$', views.tasks_overview),
]