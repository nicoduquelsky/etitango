from django.contrib import admin
from .models import Profile, User

# class ProfileAdmin(admin.ModelAdmin):
class ProfileAdminInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'email'

    list_display = ('name', 'last_name', 'dni_number', 'updated')
    list_filter = ('name', 'last_name', 'dni_number')
    # readonly_fields = ('updated')

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

# class UserAdmin(admin.ModelAdmin):
class UserAdmin(admin.ModelAdmin):
    inlines = [
        ProfileAdminInline,
    ]

    list_display = ('email', 'is_active')
    fieldsets = (
        (None, {
            'fields' : ('email', 'password', ('groups', 'user_permissions'),'is_superuser', 'is_active', 'is_staff', 'is_admin')
        }),
    )

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(UserAdmin, self).get_inline_instances(request, obj)

# admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)