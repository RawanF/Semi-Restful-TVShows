from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.root),
    url(r'^shows$', views.index),
    url(r'^shows/(?P<num>[0-9]+)$', views.DisplayShow),
    url(r'^shows/new$', views.newShow),
    url(r'^shows/(?P<num>[0-9]+)/edit$', views.editShow),
    url(r'^shows/(?P<num>[0-9]+)/destroy$', views.destroy),
]