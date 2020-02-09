from django.urls import path,include
from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name="login"),
    url(r'^logout$', views.logout, name='logout'),
    path('', views.feed, name="feed"),
    url(r'^feed/$', views.feed, name='feed'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    url(r'^auth/', include('social_django.urls', namespace='google')),
]