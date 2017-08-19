from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from Veichal.models import Car
from django.template import loader
from django.views.generic import TemplateView

app_name="Veichal"


class ListCar(ListView):
    model = Car
    template_name = "veichal/lis.html"

class CreateCar(CreateView):
    model = Car
    fields = "__all__"
class DetailCar(DetailView):
    model = Car
    template_name = 'veichal/Detail.html'




