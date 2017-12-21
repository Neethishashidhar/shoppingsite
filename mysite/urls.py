from django.conf.urls import url
from mysite import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home-view'),
    url(r'^orders/$', views.ListOrdersView.as_view(), name='order-list'),
    url(r'^CreateOrder/$', views.OrderCreate.as_view(), name='create-order'),
    url(r'^EditOrder/(?P<pk>\w+)$',
        views.OrderUpdate.as_view(), name='edit-order'),
    url(r'^DeleteOrder/(?P<pk>\w+)$',
        views.OrderDelete.as_view(), name='delete-order'),
    url(r'^GetOrdersApi/', views.OrderListAPI.as_view(),
        name='get-orders-api'),
    url(r'^CreateOrderApi/', views.OrderCreateAPI.as_view(),
        name='create-orders-api'),
]
