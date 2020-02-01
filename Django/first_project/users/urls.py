from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login_check/$', views.login_check, name='login_check'),

]
