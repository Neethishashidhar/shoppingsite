from django import forms
from .models import Organisation, Branch, Order


class CreateOrder(forms.ModelForm):
    organisation = forms.ModelChoiceField(queryset=Organisation.objects.all())
    branch = forms.ModelChoiceField(queryset=Branch.objects.all())

    class Meta:
        model = Order
        fields = ('organisation', 'branch', 'customer', 'product', 'comments')
