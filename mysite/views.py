from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .forms import OrderForm
from django.http import HttpResponseRedirect
from .models import Order
from django.views.generic.edit import FormView
from django.urls import reverse


class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ListOrdersView(generic.ListView):
    model = Order


class OrderCreate(FormView):
    template_name = 'order_form.html'
    form_class = OrderForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('order-list'))
