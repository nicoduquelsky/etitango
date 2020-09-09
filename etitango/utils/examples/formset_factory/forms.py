from django import forms
from django.forms import ModelForm, Textarea
from .models import Expenditure

class ExpenditureForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Expenditure
        fields = ('expenditure', 'description')
        widgets = {
            'description': Textarea(attrs={'cols':60, 'rows': 1}),
        }
