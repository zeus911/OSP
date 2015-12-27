from django.conf.urls import include, url
from views import select

urlpatterns = [
    url(r'^host/$', select),
]