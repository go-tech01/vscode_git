from django import forms
from django.forms import fields
from sales.models import Sale

class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('first_name', 'last_name', 'age')
 
class SalesForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)