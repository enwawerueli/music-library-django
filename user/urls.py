from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^accounts/login/$', views.account_login, name='login'),
    url(r'^accounts/logout/$', views.account_logout, name='logout'),
    url(r'^accounts/register/$', views.account_signup, name='register')
]
