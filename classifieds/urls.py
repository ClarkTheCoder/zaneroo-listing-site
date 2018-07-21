from django.conf.urls import url
# imports for views at a gloabl level (aka other django apps)
from . import views

app_name = 'classifieds'

urlpatterns = [
    url(r'^create/$', views.create, name='create_post'),
    url(r'^latest-ads/$', views.latest_ads, name='latest_ads'),
    url(r'^ad-details/(?P<ad_id>[0-9]+)/$', views.ad_details, name='ad_details'),

]
