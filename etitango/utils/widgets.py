from functools import wraps
import requests

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.forms import DateInput
from django.utils.translation import gettext_lazy as _

def check_recaptcha(view_func):
    """
    This decorator can be use in any form, even of another app. It gonna add a
    It need requests and the google keys to works well.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == 'POST':
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
                }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if result['success']:
                request.recaptcha_is_valid = True
            else:
                request.recaptcha_is_valid = False
                messages.warning(request, _('El CAPTCHA no es valido, intente nuevamente.'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

class DatePickerInput(DateInput):
    template_name = 'datepicker.html'

    def get_context(self, name, value, attrs):
        datepicker_id = 'id_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datepicker_id)
        attrs['class'] = 'form-control datepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datepicker_id'] = datepicker_id
        return context