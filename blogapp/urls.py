
from django.conf.urls import url
from blogapp.views import *

urlpatterns = [
    url(r'^$', Index, name='index'),
]
