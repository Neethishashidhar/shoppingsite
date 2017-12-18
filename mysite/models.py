from django.db import models
from django.urls import reverse


class Organisation(models.Model):

    """
    Model representing a organisation.
    """
    name = models.CharField(
        max_length=200, help_text="Enter Organisation name")

    def __str__(self):
        return self.name


class Branch(models.Model):

    """
    Model representing a Branch.
    """
    organisation = models.ForeignKey('Organisation', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, help_text="Enter Branch name")

    def __str__(self):
        return self.name


class Customer(models.Model):

    """
    Model representing a Customer
    """
    branch = models.ForeignKey('Branch', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, help_text="Enter Customer name")
    email = models.EmailField(
        help_text="Enter Email id in the form xyz@domain.com")

    def __str__(self):
        return self.name


class Product(models.Model):

    """
    Model representing a Product
    """
    name = models.CharField(max_length=200, help_text="Enter Product name")

    def __str__(self):
        return self.name


class Order (models.Model):

    """
    Model representing a order
    """
    order_id = models.AutoField(primary_key=True, editable=False)
    customer = models.ForeignKey('Customer', models.PROTECT)
    product = models.ForeignKey('Product', models.PROTECT)
    comments = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.order_id

    def get_absolute_url_for_edit(self):
        return reverse('edit-order', args=[self.order_id])

    def get_absolute_url_for_delete(self):
        return reverse('delete-order', args=[self.order_id])
