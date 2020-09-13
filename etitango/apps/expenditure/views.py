from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import Expenditure
from .forms import ExpenditureForm
from apps.profiles.models import User

from utils.defs import PanelContextMixin, PermissionContextMixin


# def expenditure_up(request):
#     submitted = False
class ExpenditureUp(PanelContextMixin, PermissionContextMixin, FormView):
    # if request.method == 'POST':
    # permission_required = ('events.add_event',)
    model = Expenditure
    form_class = ExpenditureForm
    template_name = 'expenditure/receipt.html'
    success_url = reverse_lazy('expenditure_up')

    def form_valid(self, form):
        # form = ExpenditureForm(request.POST, request.FILES)
        # if form.is_valid():
        user = User.objects.get(email=self.request.user)
        expendtype = form.cleaned_data['expendtype']
        description = form.cleaned_data['description']
        detail = form.cleaned_data['detail']
        price = form.cleaned_data['price']
        receipt = form.cleaned_data['receipt']

        expenditure_item = Expenditure(owner=user, state=False, expendtype=expendtype,
                                        description=description, detail=detail, price=price, receipt=receipt
                                        )
        expenditure_item.save()

        return super().form_valid(form)
        # return HttpResponseRedirect('/expenditure/?submitted=True?')
    # else:
    #     form = ExpenditureForm()
    #     if 'submitted' in request.GET:
    #         submitted = True



    # return render(request, 'expenditure/receipt.html', {'form' : form, 'submitted' : submitted})
