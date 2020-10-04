from django.contrib import admin
from .models import Expenditure

class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('owner', 'expendtype', 'price')

    fieldsets = (
        (None, {
            'fields' : (('owner', 'expendtype'), 'description', 'detail', ('price', 'state'), 'receipt')
        }),
    )

admin.site.register(Expenditure, ExpenditureAdmin)
