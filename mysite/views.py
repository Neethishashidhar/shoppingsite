from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from mysite.serializers import OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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


class OrderListAPI(APIView):

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderCreateAPI(APIView):

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
