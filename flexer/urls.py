from django.conf.urls import url
from . import views
from flexer import views

urlpatterns = [
    #url(r'^', views.index, name='index'),
    url(r'^snippets/$', views.snippet_list),
    url(r'^users/$', views.user_list),
    url(r'^tasks/$', views.manage_tasks),
    url(r'^tasksdel/', views.delete_tasks),
]