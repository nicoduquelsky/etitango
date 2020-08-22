from django.contrib import admin
from .models import Expenditure

class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('owner', 'eti_event', 'expendtype', 'price')

    fieldsets = (
        (None, {
            'fields' : (('owner', 'eti_event', 'expendtype'), 'description', 'detail', ('price', 'state'), 'receipt')
        }),
    )

admin.site.register(Expenditure, ExpenditureAdmin)
