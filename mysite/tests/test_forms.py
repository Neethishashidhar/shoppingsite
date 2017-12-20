from django.test import TestCase
from mysite.forms import OrderForm
from mysite.models import Order, Organisation, Branch, Customer, Product


class OrderFormTest(TestCase):

    def test_form(self):
        org = Organisation(name="organisation11")
        br = Branch(organisation=org, name="branch1")
        cust = Customer(branch=br, name="customer1", email="cust1@xyz.com")
        prod = Product(name="prod1")
        order = Order(
            order_id="234",
            customer=cust,
            product=prod,
            comments="asdjhsgd")
        form = OrderForm({'order_id': '234',
                          'customer': '1',
                          'product': '1',
                          'comments': "asdjhsgd"}, instance=order)
        self.assertEquals(form.data, {'order_id': '234',
                          'customer': '1',
                          'product': '1',
                          'comments': "asdjhsgd"})
