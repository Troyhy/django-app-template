from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import *
from views import app_index

urlpatterns = patterns('',
    url(r'^$', app_index, name='app_index'),
)

