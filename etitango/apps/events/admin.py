from django.contrib import admin
from .models import Event, Inscription
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('staff', 'group', 'eti_name')
    #Fields in admin to edit-add
    fieldsets = (
        (None, {
            'fields' : (('staff', 'group'), 'eti_name', 'description', 
            'begin_date', ('country', 'province', 'city'))
        }),
        ('Inscripciones', {
            'fields' : (('open_date', 'close_date'),
             ('register_total', 'register_limit'),
             'active', 'cancelation')
        })
    )

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'eti', 'staff_flag', 'raffled')

    fieldsets = (
        (None, {
            'fields' : (('email', 'eti'), 'staff_flag', 'staff_task')
        }),
        ('Información Personal', {
            'fields' : (('rol', 'food', 'transportation'), 'number_underage')
        }),
        ('Información del Evento', {
            'fields' : (('arrival_date', 'leave_date'), 'inscription_date', 
            ('cession_user', 'cession_verification_id_organizater'), 
            ('raffled', 'cancelled'), 'help_with', 'extra_details')
        }),
    )

admin.site.register(Event, EventAdmin)
admin.site.register(Inscription, InscriptionAdmin)