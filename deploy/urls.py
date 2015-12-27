from django.conf.urls import include, url
from views import index, deploy

urlpatterns = [
    url(r'^$', index),
    url(r'^api/$', deploy, name='deploy_work'),
]