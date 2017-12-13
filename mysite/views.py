from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from .models import Order


class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ListOrdersView(generic.ListView):
    model = Order
