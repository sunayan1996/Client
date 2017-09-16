from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^maps', views.index1, name='index1'),
    url(r'^well', views.well, name='well'),
    url(r'^household', views.household, name='household'),
    url(r'^landlord', views.landlord, name='landlord'),
    url(r'^farms', views.farms, name='farms'),
    url(r'^home', views.home, name='home'),
]
