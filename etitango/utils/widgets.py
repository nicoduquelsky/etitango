from django.forms import DateInput

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