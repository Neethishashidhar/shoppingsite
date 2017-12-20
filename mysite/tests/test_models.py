
from django.test import TestCase
from mysite.models import Organisation, Branch, Customer, Product, Order


class OrganisationModelTest(TestCase):

    def setUp(self):
        self.org = Organisation.objects.create(name='Test Organisation')

    def test_organisation_field(self):
        value = self.org.name
        self.assertEquals(value, 'Test Organisation')

    def test_org_name_max_length(self):
        length = self.org._meta.get_field('name').max_length
        self.assertEquals(length, 200)


class BranchModelTest(TestCase):

    def setUp(self):
        self.org = Organisation.objects.create(name='Organisation1')
        Branch.objects.create(organisation=self.org, name='Branch1')

    def test_branch_fields(self):
        branch = Branch.objects.get(id=1)
        self.assertEquals(str(branch.organisation), 'Organisation1')
        self.assertEquals(branch.name, 'Branch1')

    def test_branch_name_max_length(self):
        length = Branch._meta.get_field('name').max_length
        self.assertEquals(length, 200)


class CustomerModelTest(TestCase):

    def setUp(self):
        self.org = Organisation.objects.create(name='Organisation1')
        self.branch = Branch.objects.create(
            organisation=self.org,
            name='Branch1')
        self.cust = Customer.objects.create(
            branch=self.branch,
            name='Customer1',
            email='Cust1@xyz.com')

    def test_customer_fields(self):
        self.assertEquals(str(self.branch.organisation), 'Organisation1')
        self.assertEquals(str(self.cust.branch), 'Branch1')
        self.assertEquals(self.cust.email, 'Cust1@xyz.com')

    def test_cust_name_max_length(self):
        length = self.cust._meta.get_field('name').max_length
        self.assertEquals(length, 200)


class ProductModelTest(TestCase):

    def setUp(self):
        self.prod = Product.objects.create(name='Product1')

    def test_product_field(self):
        value = self.prod.name
        self.assertEquals(value, 'Product1')

    def test_prod_name_max_length(self):
        length = self.prod._meta.get_field('name').max_length
        self.assertEquals(length, 200)


class OrderModelTest(TestCase):

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

    def test_order_fields(self):
        self.assertEquals(self.order.order_id, '234')
        self.assertEquals(str(self.prod), 'Product1')
        self.assertEquals(str(self.cust), 'Customer1')
        self.assertEquals(self.order.comments, 'This is a comment')

    def test_get_absolute_url_for_edit(self):
        self.assertEquals(
            self.order.get_absolute_url_for_edit(),
            '/EditOrder/234')

    def test_get_absolute_url_for_delete(self):
        self.assertEquals(
            self.order.get_absolute_url_for_delete(),
            '/DeleteOrder/234')

    def test_order_comments_max_length(self):
        length = self.order._meta.get_field('comments').max_length
        self.assertEquals(length, 300)
