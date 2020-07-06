from django.shortcuts import render

from .models import Country, Province, City

# LOCATION
def load_provinces(request):
    country = request.GET.get('country')
    countryMid = Country.objects.get(id=country).country_id
    provinces = Province.objects.filter(country_id=countryMid).order_by('province_name')
    return render(request, 'hr/provinces_dropdown_list_options.html', {'provinces': provinces })

def load_cities(request):
    province = request.GET.get('province')
    provinceMid = Province.objects.get(id=province)
    cities = City.objects.filter(province_id=provinceMid).order_by('city_name')
    return render(request, 'hr/cities_dropdown_list_options.html', {'cities': cities })
