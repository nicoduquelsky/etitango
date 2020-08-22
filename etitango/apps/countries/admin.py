from django.contrib import admin
from .models import Country, City, Province

class CountryAdmin(admin.ModelAdmin):
    pass

class ProvinceAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)

