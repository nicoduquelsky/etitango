from django.db import models

class City(models.Model):
    province          = models.ForeignKey('Province', on_delete=models.PROTECT, null=True)
    city_name         = models.CharField(max_length=32, null=True)
    capital_flag      = models.BooleanField(default=False)
    zone              = models.DecimalField(max_digits=1, decimal_places=0, null=True)

    def __str__(self):
        return self.city_name

class Country(models.Model):
    country_id        = models.CharField(max_length=2, null=True, unique=True)
    country_name      = models.CharField(max_length=32, null=True, unique=True)

    def __str__(self):
        return self.country_name

class Province(models.Model):
    province_name     = models.CharField(max_length=32, null=True, unique=True)
    country           = models.ForeignKey('Country', to_field='country_id', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.province_name
