from django.conf.urls import url
from . import views , by_main_result
from django.urls import path , include
app_name = 'search'



urlpatterns = [
    # url(r'^(?P<catugry_1>[\w-]+)/$',views.by_catugry, name='by_catugry') ,
    url(r'^$', views.by_catugry, name='by_catugry'),# <-- this one here #
    url(r'^main/(?P<main_id_>\d+)$', views.by_main_all , name='by_main_all'),
    url(r'main/ajax/', by_main_result.by_main_result , name='by_main_result'),
    url(r'main/change_form/ajax/', by_main_result.change_form_search , name='change_form_search'),

]
