from django.conf.urls import url, include
from . import views
from personal.views import PostView

urlpatterns = [
    url(r'^$', PostView.as_view(), name='index'),
    url(r'^contact/$', views.contact, name='contact'),
]
