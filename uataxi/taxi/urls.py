from django.conf.urls import patterns, url
from taxi import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^city/(?P<city_id>\d+)/$', views.city, name='city'),
    url(r'^taxi/(?P<taxi_id>\d+)/$', views.taxi, name='taxi')
)
