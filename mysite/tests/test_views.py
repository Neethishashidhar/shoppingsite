from django.test import TestCase
from mysite.models import Order, Organisation, Branch, Customer, Product
from django.urls import reverse
from mysite.serializers import OrderSerializer


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
            order_id='234',
            customer=self.cust,
            product=self.prod,
            comments="This is a comment")
        self.order.save()

    def test_list(self):
        resp = self.client.get(reverse('order-list'))
        self.assertEqual(len(resp.context['order_list']), 1)

    def test_order_list_page(self):
        resp = self.client.get('/orders/')
        self.assertEqual(resp.status_code, 200)


class OrderListAPITest(TestCase):

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
            order_id='234',
            customer=self.cust,
            product=self.prod,
            comments="This is a comment")
        self.order.save()

    def test_get_all_orders(self):
        response = self.client.get(reverse('get-orders-api'))
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertNotEqual(response.data, serializer.data)
        self.assertNotEqual(response.status_code, 200)


class OrderCreateAPITests(TestCase):

    def test_create_order(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('create-orders-api')
        data = {
            'order_id': '234',
            'customer': '1',
            'product': '1',
            'comments': 'this is a comment'}
        response = self.client.post(url, data, format='json')
        self.assertNotEqual(response.status_code, 200)
        self.assertNotEqual(Order.objects.count(), 1)
