from django.conf.urls import url
from . import views
app_name = 'user_profile'
urlpatterns = [
    # url(r'^$',views.all_ads, name='all_ads') ,
    url(r'^$',views.user_profile_sittings, name='user_profile_sittings') ,
    url(r'^favoret$', views.favoret , name='favoret'),
    # url(r'^creat$', views.creat_ads , name='creat_ads'),
    # url('ajax/load-cities/', views.load_sub, name='load_sub'),# <-- this one here #
    # url('ajax/change_form/', views.change_form, name='change_form'),   # <-- this one here
    # url(r'^(?P<id>\d+)/edit$', edit.edit_ads, name='edit_ads'),
    # url(r'^$',views.all_post, name='all_post' ) ,
    # url(r'^del/(?P<id>\d+)$', views.del_post, name='del_post'),
    # url(r'^test$', views.test, name='test'),

]
