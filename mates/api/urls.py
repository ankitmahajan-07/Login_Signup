from django.urls import path,include
from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^api/users', views.listUsers.as_view(), name='api-users'),
    url(r'^(?P<pk>[\W-]+)/$', views.RetrieveDetailsView.as_view(), name='api-user-details'),
]