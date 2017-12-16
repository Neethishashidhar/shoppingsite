from django import forms
from .models import Organisation, Branch, Order, Customer


class OrderForm(forms.ModelForm):
    organisation = forms.ModelChoiceField(
        queryset=Organisation.objects.all(),
        widget=forms.Select(attrs={"onChange": 'loadbranch()'}))
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.values('id',
                                       'name',
                                       'organisation_id'),
        widget=forms.Select(attrs={"onChange": 'loadcustomer()'}))
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    cust = forms.ModelChoiceField(
        queryset=Customer.objects.values(
            'id',
            'name',
            'branch_id'),
        required=False)

    class Meta:
        model = Order
        fields = ('organisation', 'branch', 'customer', 'product', 'comments')
