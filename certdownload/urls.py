from django.conf.urls import url, include
from . import views

app_name = "cert_download"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^download/$', views.download, name='download'),
]
