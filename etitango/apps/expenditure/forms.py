from django.forms import ModelForm
from .models import Expenditure

class ExpenditureAddForm(ModelForm):
    class Meta:
        model = Expenditure
        fields = [
            'expendtype', 'description', 
            'detail', 'price', 'receipt'
        ]