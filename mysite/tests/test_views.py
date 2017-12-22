from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from mysite.models import Order, Organisation, Branch, Customer, Product
from mysite.serializers import OrderSerializer
from rest_framework.test import APIClient, APITestCase


class HomePageViewTest(TestCase):

    def test_home_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home-view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')


class ListOrdersViewTest(TestCase):

    def setUp(self):
        self.org = Organisation.objects.create(name='Organisation1')
        self.branch = Branch.objects.create(
            organisation=self.org,
            name='Branch1')
        self.cust = Customer.objects.create(
            branch=self.branch,
            name='Customer1',
            email='Cust1@xyz.com')
        self.prod = Product.objects.create(name='Product1')
        self.order = Order.objects.create(
            order_num='abcd123f',
            customer=self.cust,
            product=self.prod,
            comments="This is a comment")
        self.order.save()

    def test_order_list(self):
        resp = self.client.get(reverse('order-list'))
        self.assertEqual(len(resp.context['order_list']), 1)

    def test_order_list_by_name(self):
        resp = self.client.get(reverse('order-list'))
        self.assertEqual(resp.status_code, 200)


class OrderCreateViewTest(TestCase):

    def setUp(self):
        self.org = Organisation.objects.create(id='1', name='Organisation1')
        self.branch = Branch.objects.create(
            id='1',
            organisation=self.org,
            name='Branch1')
        self.cust = Customer.objects.create(
            id='1',
            branch=self.branch,
            name='Customer1',
            email='Cust1@xyz.com')
        self.prod = Product.objects.create(id='1', name='Product1')

    def test_create_order_page(self):
        url = reverse('create-order')
        data = {
            'organisation': 1,
            'branch': 1,
            'customer': 1,
            'product': 1,
            'comments': 'this is a comment'}
        self.client.post(url, data, format='json')
        self.assertEqual(Order.objects.count(), 1)


class OrderEditViewTest(TestCase):

    def setUp(self):
        self.org = Organisation.objects.create(id='1', name='Organisation1')
        self.branch = Branch.objects.create(
            id='1',
            organisation=self.org,
            name='Branch1')
        self.cust = Customer.objects.create(
            id='1',
            branch=self.branch,
            name='Customer1',
            email='Cust1@xyz.com')
        self.prod = Product.objects.create(id='1', name='Product1')
        self.order = Order.objects.create(
            id='1',
            order_num='ghtdf23v',
            customer=self.cust,
            product=self.prod,
            comments="This is a comment")

    def test_edit_order_page(self):
        url = '/EditOrder/1'
        data = {
            'organisation': 1,
            'branch': 1,
            'customer': 1,
            'product': 1,
            'comments': 'comment changed'}
        self.client.post(url, data, format='json')
        self.assertEqual(Order.objects.get(id=1).comments, data['comments'])


class OrderDeleteViewTest(TestCase):

    def setUp(self):
        self.org = Organisation.objects.create(id='1', name='Organisation1')
        self.branch = Branch.objects.create(
            id='1',
            organisation=self.org,
            name='Branch1')
        self.cust = Customer.objects.create(
            id='1',
            branch=self.branch,
            name='Customer1',
            email='Cust1@xyz.com')
        self.prod = Product.objects.create(id='1', name='Product1')
        self.order = Order.objects.create(
            id='1',
            order_num='ghtdf23v',
            customer=self.cust,
            product=self.prod,
            comments="This is a comment")

    def test_delete_order_page(self):
        url = '/DeleteOrder/1'
        data = {
            'organisation': 1,
            'branch': 1,
            'customer': 1,
            'product': 1,
            'comments': 'comment changed'}
        self.client.post(url, data, format='json', follow=True)
        self.assertEqual(Order.objects.count(), 0)


class OrderListAPITest(APITestCase):

    def setUp(self):
        self.org = Organisation.objects.create(id='1', name='Organisation1')
        self.branch = Branch.objects.create(
            id='1',
            organisation=self.org,
            name='Branch1')
        self.cust = Customer.objects.create(
            id='1',
            branch=self.branch,
            name='Customer1',
            email='Cust1@xyz.com')
        self.prod = Product.objects.create(id='1', name='Product1')
        self.order = Order.objects.create(
            customer=self.cust,
            product=self.prod,
            comments="This is a comment")
        self.order.save()
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')
        self.client = APIClient()

    def test_get_all_orders_with_authentication(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('get-orders-api'))
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_orders_without_authentication(self):
        response = self.client.get(reverse('get-orders-api'))
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertNotEqual(response.data, serializer.data)
        self.assertNotEqual(response.status_code, 200)


class OrderCreateAPITests(APITestCase):

    def setUp(self):
        self.org = Organisation.objects.create(id='1', name='Organisation1')
        self.branch = Branch.objects.create(
            id='1',
            organisation=self.org,
            name='Branch1')
        self.cust = Customer.objects.create(
            id='1',
            branch=self.branch,
            name='Customer1',
            email='Cust1@xyz.com')
        self.prod = Product.objects.create(id='1', name='Product1')
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')
        self.client = APIClient()
        self.data = {
            'customer': 1,
            'product': 1,
            'comments': 'this is a comment'}

    def test_create_order_with_authentication(self):
        url = reverse('create-orders-api')
        data = {
            'customer': 1,
            'product': 1,
            'comments': 'this is a comment'}

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, data)
        self.assertEqual(Order.objects.count(), 1)

    def test_create_order_without_authentication(self):
        url = reverse('create-orders-api')
        response = self.client.post(url, self.data, format='json')
        self.assertNotEqual(response.data, self.data)
        self.assertNotEqual(Order.objects.count(), 1)
