from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Expenditure
from .forms import ExpenditureAddForm
from apps.profiles.models import User

from utils.defs import PanelContextMixin, PermissionContextMixin
from utils.image_utils import reduce_image_size


class ExpenditureAdd(PanelContextMixin, PermissionContextMixin, CreateView):
    model = Expenditure
    form_class = ExpenditureAddForm
    template_name = 'expenditure/add_expend.html'
    success_url = reverse_lazy('expenditure_add')

    def form_valid(self, form):
        form.instance.owner = self.request.user

        receipt = reduce_image_size(form.cleaned_data['receipt'], new_size=(720, 720))
        form.instance.receipt = receipt
        form.instance.state = False
        form.save()
                
        return super().form_valid(form)