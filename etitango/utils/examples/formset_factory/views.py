from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory

from .models import Expenditure
from .forms import ExpenditureForm

def load_expenditure(request):
    ExpenditureFormSet = modelformset_factory(
        Expenditure, fields=('expenditure', 'description'),
        form = ExpenditureForm, extra=1)
    formset = ExpenditureFormSet(queryset=Expenditure.objects.none())
    #formset = ExpenditureFormSet()         # use this to instantiate saved forms on the database
    if request.method == 'POST':
        formset = ExpenditureFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect('/expenditure/?submitted=True')
    return render(request, 'expenditures/expenditure.html',
        {'formset':formset, 'base_form':ExpenditureForm()})