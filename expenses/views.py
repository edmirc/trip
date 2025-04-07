from django.shortcuts import render
from expenses.models import Car, Citys

from expenses.forms import CarForm, CityForm
from django.views.generic import FormView 


class CarView(FormView):
    template_name = 'car.html'
    form_class = CarForm
    success_url = '/car/'
    queryset = Car.objects.all()
    context_object_name = 'cars'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CitysViews(FormView):
    template_name = 'city.html'
    form_class = CityForm
    success_url = '/city/'
    queryset = Citys.objects.all()
    context_object_name = 'citys'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

