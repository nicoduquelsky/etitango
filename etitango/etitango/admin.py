from django.contrib import admin
# from django.contrib.auth.models import Group

#Models to register in Admin
from apps.events.models import Event, Inscription
from apps.profiles.models import Profile, User
from apps.expenditure.models import Expenditure
from apps.countries.models import City, Country, Province
from apps.blog.models import Blog

from utils.perms import Create_SuperGroups

Create_SuperGroups()


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'last_name', 'dni_number', 'updated')
    list_filter = ('name', 'last_name', 'dni_number')
    # readonly_fields = ('updated')

    fieldsets = (
        (None,{
            'fields' : ('email', ('name', 'last_name'), 'avatar', 'updated')
        }),

        ('Personal Information',{
            'classes' : ('wide',),
            'fields' : (('dni_number', 'dni_type'), 'birth_date', 'gender')

        }),

        ('Location',{
            'classes' : ('wide',),
            'fields' : ('country', 'province', 'city')
        }),
    )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)
admin.site.register((Event, Inscription, Expenditure, City, Country, Province, Blog))