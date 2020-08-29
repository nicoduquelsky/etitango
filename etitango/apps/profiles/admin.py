from django.contrib import admin
from .models import Profile, User

#Include Profile form in user form. Add and change User in conjuction with  Profile.
'''Because signals are used, when a user is created a profile is created simultaneously.
If Profile form is not included in User form, an error is generated with the uniques files in Profile.
If Profile doesn't have Unique it might not be put as inlines.
'''
class ProfileAdminInline(admin.StackedInline):
    model = Profile #Model reference
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'email' #Model foreign key

    list_display = ('name', 'last_name', 'dni_number', 'updated')
    list_filter = ('name', 'last_name', 'dni_number') #Fields to order information in shown list
    
    #Fields in admin to edit-add
    fieldsets = (
        (None,{
            'fields' : (('name', 'last_name'), 'avatar', 'updated')
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

class UserAdmin(admin.ModelAdmin):
    #Include Profile form in User form
    inlines = [
        ProfileAdminInline,
    ]

    list_display = ('email', 'is_active')
    fieldsets = (
        (None, {
            'fields' : ('email', 'password', ('groups', 'user_permissions'),'is_superuser', 'is_active', 'is_staff', 'is_admin')
        }),
    )

admin.site.register(User, UserAdmin)