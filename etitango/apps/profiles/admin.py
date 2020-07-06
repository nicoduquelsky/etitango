# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#
# from .models import User       # all, for dev
# from .forms import UserAdminCreationForm, UserAdminChangeForm
#
#
# User = get_user_model()
#
# class UserAdmin(PermissionRequiredMixin, BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'is_admin')
#     list_filter = ('is_admin', 'is_staff', 'is_active')
#     fieldsets = (
#         (None, {'fields': ('email',)}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
# # admin.site.register(User, UserAdmin)
