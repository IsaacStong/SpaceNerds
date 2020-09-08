from django.urls import path, repath
from . import views

app_name = 'groups'

#urlpatterns for groups app
url_patterns = [
    re_path(r'^$', views.ListGroups.as_view(), name='all'),
    re_path(r'^new/$', views.CreateGroup.as_view(), name='create'),
    re_path(r'posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
]
