from django.forms import ModelForm, Textarea, BooleanField

# APPS
from apps.countries.models import Province, Country, City
from apps.profiles.models import User

# UTILS
from utils import choices
from utils.defs import PanelContextMixin, PermissionContextMixin

# SELF
from .models import Event, Inscription, EventGroup


EVENT_FIELDS = ['eti_name', 'description', 'begin_date', 'country',
                'province', 'city', 'open_date', 'close_date',  'register_limit', ]
INSCRIPTION_FIELDS = ['rol', 'food', 'transportation',
                      'number_underage', 'arrival_date', 'leave_date', 'help_with', 'extra_details'] # 'eti' was removed

class EventForm(PanelContextMixin, PermissionContextMixin, ModelForm):
    # Only Boss Users can access.
    permission_required = ('event.add_event',)
    # Locations work with data.choices
    country = choices.CountryModelChoiceField(
        queryset=choices.Country.objects.all(), required=False, label="País")
    province = choices.ProvinceModelChoiceField(
        queryset=choices.Province.objects.all(), required=False, label="Provincia")
    city = choices.CityModelChoiceField(
        queryset=choices.City.objects.all(), required=False, label="Ciudad")

    class Meta:
        model   = Event
        fields  = EVENT_FIELDS
        widgets = {
                    'begin_date': choices.DateInput(),
                    'open_date': choices.DateInput(),
                    'close_date': choices.DateInput(),
         }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Location fields work with scripts in the template level.
        self.fields['province'].queryset = Province.objects.none()
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            if 'country' in self.data == 'NULL':
                self.fields['city'].queryset = City.objects.none()
                return
            try:
                country_id = int(self.data.get('country'))
                countryMid = Country.objects.get(id=country_id).country_id
                self.fields['province'].queryset = Province.objects.filter(
                    country_id=countryMid).order_by('province_name')
            except (ValueError, TypeError):
                pass

            if 'province' in self.data:
                if 'province' in self.data == 'NULL':
                    self.fields['city'].queryset = City.objects.none()
                    return
                try:
                    province_id = int(self.data.get('province'))
                    provinceMid = Province.objects.get(id=province_id)
                    self.fields['city'].queryset = City.objects.filter(
                        province_id=provinceMid).order_by('city_name')
                except (ValueError, TypeError):
                    pass

    def save(self, commit=True):
        event = super(EventForm, self).save(commit=False)
        if commit:
            """
                Save method for edit and create events
                1) Check if Boss User has a event created yet.
                2) Else, it create the Group first.
                3) Then, the event is associated to group, by its ForeignKey.
                4) Now:
                + Event got a staff_id and group_id
                + Group and Event share "eti_name".
                + staff_id o group_id are uniques for events.

                If Boss created a event before, save method work with it.
            """

            if not Event.objects.filter(staff=self.instance.staff):
                EventGroup.objects.save(name=event.eti_name)
                event.group = EventGroup.objects.get(name__iexact=event.eti_name)
                event.save()
            else:
                event = Event.objects.filter(staff_id__exact=self.instance.staff_id).update(**self.cleaned_data)

        return event

class EventActiveForm(PanelContextMixin, PermissionContextMixin, ModelForm):
    permission_required = ('event.change_event',)
    active = BooleanField(required=True, label="¡Activar evento!")

    class Meta:
        model  = Event
        fields = ('active',)

    def save(self, commit=False):
        if Event.objects.filter(staff=self.instance.staff):
            event = Event.objects.filter(staff_id__exact=self.instance.staff_id).update(active=True)
        return event

class InscriptionForm(PanelContextMixin, ModelForm):
    """
        Eti inscriptions support multievent, but we are filter it
        Until site need that functions.
    """
    # eti = choices.EtiModelChoiceField(Event.objects.filter(active='True'), required=True)
    # eti = Event.objects.filter(active='True')

    class Meta:
        model   = Inscription
        fields  = INSCRIPTION_FIELDS
        widgets = {
                    'arrival_date': choices.DateInput(),
                    'leave_date': choices.DateInput(),
                    'close_date': choices.DateInput(),
                    'extra_details': Textarea(),
         }
