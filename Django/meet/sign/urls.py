from django.conf.urls import url
from . import views

app_name = 'sign'
urlpatterns = [
    url(r'^test_response', views.test_response, name='test_response'),

    url(r'^is_new_user/$', views.is_new_user, name='is_new_user'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^sign/$', views.sign, name='sign'),
    url(r'^refuse_attend/$', views.refuse_attend, name='refuse_attend'),
    url(r'^get_user_today_meets/$', views.get_user_today_meets, name='get_user_today_meets'),
    url(r'^get_sign_statistics/$', views.get_sign_statistics, name='get_sign_statistics'),
    url(r'^get_detail_groups/$', views.get_detail_groups, name='get_detail_groups'),
]
