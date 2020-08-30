from django import forms

from datetime import date

# APPS
from apps.countries.models import Country, Province, City

# CONTANTS
GENDER_CHOICES = (
    ('M', ("Male")),
    ('F', ("Female")),
    ('O', ("Others")),
)

DNI_TYPE_CHOICES = (
    ('DNI', ("DNI")),
    ('CI-', ("CI-")),
    ('PAS', ("PASSAPORT")),
)

ROL_CHOICES = (
    ('L', ("Lidera")),
    ('F', ("Sigue")),
    ('A', ("Indistinto")),
)

FOOD_CHOICES = (
    ('O', ("Omnívora/Carnivora")),
    ('C', ("Sin Gluten")),
    ('V', ("Vegetariana")),
    ('G', ("Vegana")),
)

TRANSPORTATION_CHOICES = (
    ('A', ("Auto")),
    ('B', ("Colectivo")),
    ('V', ("Avión")),
    ('C', ("Combi")),
    ('O', ("Otro")),
)

HELP_WITH_CHOICES = (
    ('B', ("Barra")),
    ('C', ("Cocina")),
    ('A', ("Armado del Salon")),
)

# CLASS
class CountryModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.country_name

class ProvinceModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.province_name

class CityModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.city_name

class EtiModelChoiceField(forms.ModelChoiceField):
    """
    We could return a dropdown events opens here, using something like:
    # def label_from_instance(self,obj):
        # return obj.eti_name

    While our site is still for only one event open at a time, we gonna filter it by its active flag
    """
    def label_from_instance(self, obj):
        if obj.active == True:
            return obj.eti_name
        else:
            return False

            
