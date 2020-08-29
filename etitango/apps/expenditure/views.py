from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Expenditure
from .forms import ExpenditureForm

def expenditure_up(request):
    submitted = False

    if request.method == 'POST':
        form = ExpenditureForm(request.POST, request.FILES)

        if form.is_valid():
            expendtype = form.cleaned_data['expendtype']
            description = form.cleaned_data['description']
            detail = form.cleaned_data['detail']
            price = form.cleaned_data['price']
            receipt = form.cleaned_data['receipt']

            expenditure_item = Expenditure(owner='Some ramdon dude', state=False, expendtype=expendtype,
                                            description=description, detail=detail, price=price, receipt=receipt
                                            )
            expenditure_item.save()
            return HttpResponseRedirect('/expenditure/?submitted=True?')
    else:
        form = ExpenditureForm()
        if 'submitted' in request.GET:
            submitted = True



    return render(request, 'expenditure/receipt.html', {'form' : form, 'submitted' : submitted})
