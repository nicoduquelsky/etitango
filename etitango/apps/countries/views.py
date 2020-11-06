from django.shortcuts import render

from .models import Country, Province, City

# LOCATION


def load_provinces(request):
    country_id = request.GET.get('country')
    provinces = Province.objects.filter(
        country_id=country_id).order_by('province_name')
    return render(request, 'hr/provinces_dropdown_list_options.html', {'provinces': provinces})


def load_cities(request):
    province_id = request.GET.get('province')
    cities = City.objects.filter(
        province_id=province_id).order_by('city_name')
    return render(request, 'hr/cities_dropdown_list_options.html', {'cities': cities})
