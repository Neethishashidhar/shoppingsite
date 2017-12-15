from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .forms import CreateOrder
from django.http import HttpResponseRedirect
from .models import Order


class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ListOrdersView(generic.ListView):
    model = Order


class CreateAnOrder(TemplateView):

    def create(request):
        if request.method == 'POST':
            form = CreateOrder(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/orders/')
        else:
            form = CreateOrder()

        return render(request, 'mysite/create_order.html', {'form': form})
