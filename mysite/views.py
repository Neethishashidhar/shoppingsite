from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView, DeleteView

from .forms import OrderForm
from .models import Order


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


class OrderUpdate(UpdateView):
    model = Order
    fields = ['customer', 'product', 'comments']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('order-list')


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')
