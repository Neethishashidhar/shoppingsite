from django.conf.urls import url
from mysite import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^orders/$', views.ListOrdersView.as_view(), name='order-list'),
    url(r'^CreateOrder/$', views.OrderCreate.as_view()),
]
