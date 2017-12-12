# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Organisation(models.Model):
    """
    Model representing a organisation. 
    """
    name = models.CharField(primary_key=True,max_length=200, help_text="Enter Organisation name")
    
    def __str__(self):
        return self.name
    
class Branch(models.Model):
    """
    Model representing a Branch. 
    """
    name = models.CharField(primary_key=True,max_length=200, help_text="Enter Branch name")
    org_name = models.ForeignKey('Organisation', on_delete=models.PROTECT, null= False)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    """
    Model representing a Customer 
    """
    name = models.CharField(max_length=200, help_text="Enter Customer  name")
    email_id = models.EmailField(primary_key=True, help_text="Enter Email id in the form xyz@domain.com")
    branch_name = models.ForeignKey('Branch', on_delete=models.PROTECT, null= False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Model representing a Product 
    """
    name = models.CharField(max_length=200, help_text="Enter Product  name")
    
    def __str__(self):
        return self.name

class Order (models.Model):
    """
    Model representing a order
    """
    order_id = models.AutoField(primary_key=True,editable=False)
    cust_name = models.ForeignKey('Customer', on_delete=models.PROTECT, null= False)
    product_name = models.ForeignKey('Product', on_delete=models.PROTECT, null= False)
    comments = models.TextField(max_length=300,null= True)