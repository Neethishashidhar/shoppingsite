# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Organisation,Branch,Customer,Order,Product

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
        
class ListOrdersView(generic.ListView):
    model = Order

