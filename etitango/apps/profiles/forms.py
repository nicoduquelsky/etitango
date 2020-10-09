from django import forms
from django.forms import ModelForm, BaseModelFormSet, formset_factory
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _

# APPS
from apps.countries.models import Province, Country, City

# UTILS
from utils import choices
from utils.defs import PanelContextMixin, PermissionContextMixin
from utils.widgets import DatePickerInput

# SELF
from .models import User, Profile

# CONTANTS
PROFILES_FIELDS = ['name', 'last_name', 'dni_type', 'dni_number', 'gender',
                   'birth_date', 'country', 'province', 'city', ]

# CLASSES

class UserAdminCreationForm(ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

class RegisterForm(ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False
        if commit:
            user.save()
        return user

# PROFILES
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', )

class ProfileForm(ModelForm):
    country = choices.CountryModelChoiceField(
        queryset=choices.Country.objects.all(), required=True, label="País")
    province = choices.ProvinceModelChoiceField(
        queryset=Province.objects.all(), required=False, label="Provincia")
    city = choices.CityModelChoiceField(
        queryset=choices.City.objects.all(), required=False, label="Ciudad")
    birth_date = forms.DateField(
        widget=DatePickerInput(), input_formats=['%m/%d/%Y'], required=True, label="Fecha de Nacimiento")

    class Meta:
        model = Profile
        fields = PROFILES_FIELDS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'country' in self.data:
            try:
                country_id = Country.objects.get(
                    id=int(self.data.get('country'))).country_id
                self.fields['province'].queryset = Province.objects.filter(
                    country_id=country_id).order_by('province_name')
            except (ValueError, TypeError):
                pass

            if 'province' in self.data:
                try:
                    province_id = Province.objects.get(
                        id=int(self.data.get('province')))
                    self.fields['city'].queryset = City.objects.filter(
                        province_id=province_id).order_by('city_name')
                except (ValueError, TypeError):
                    pass


class PhotoForm(ModelForm):
    avatar = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('avatar',)


# GROUPS
class GroupMembersForm(PanelContextMixin, PermissionContextMixin, ModelForm):
    members = forms.EmailField(label="editor", required=True)

    class Meta:
        model   = Profile
        fields  = ('members',)
