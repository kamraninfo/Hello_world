from django.conf.urls import url,include
from django.contrib import admin
from Veichal.views import CreateCar,ListCar,DetailCar


app_name = 'veichal'

urlpatterns = [



    url(r'^$',ListCar.as_view(),name='car-list'),

    url(r'^car/(?P<pk>\d+)$', DetailCar.as_view(), name='car-detail'),
    url(r'^car/add/', CreateCar.as_view(), name="car-add"),

]