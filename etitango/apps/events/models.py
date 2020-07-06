from django.contrib.auth.models import Group, GroupManager, Permission
from django.conf import settings
from django.db import models
from datetime import date

# APPS
from apps.data.perms import EventGroup_Perms
from apps.data.models import Country, City, Province
from apps.data import choices

from apps.profiles.models import User

class Event(models.Model):
    staff               = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group               = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupo")
    eti_name            = models.CharField(max_length=32, blank=True, null=True, verbose_name="Nombre del Evento")
    description         = models.CharField(max_length=32, blank=True, null=True, verbose_name="Descripción")
    begin_date          = models.DateField(blank=True, null=True, verbose_name="Fecha de Inicio")
    country             = models.ForeignKey(Country, on_delete=models.SET_NULL, to_field='country_id', null=True, verbose_name="País")
    province            = models.ForeignKey(Province, on_delete=models.SET_NULL, to_field='id', null=True, verbose_name="Provincia")
    city                = models.ForeignKey(City, on_delete=models.SET_NULL, to_field='id', null=True, verbose_name="ciudad")
    open_date           = models.DateField(blank=True, null=True, verbose_name="Apertura de Inscripciones")
    close_date          = models.DateField(blank=True, null=True, verbose_name="Cierre de Inscripciones")
    register_total      = models.DecimalField(max_digits=5, decimal_places=0, null=True, verbose_name="Inscripciones Totales")
    register_limit      = models.DecimalField(max_digits=5, decimal_places=0, null=True, verbose_name="Límite de Inscripciones")
    active              = models.BooleanField(default=False, verbose_name="Activo")
    cancelation         = models.CharField(max_length=32, blank=True, null=True, verbose_name="Cancelación")

class Inscription(models.Model):
    email               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    eti                 = models.ForeignKey(Event, on_delete=models.CASCADE, to_field='id', null=False)
    staff_flag          = models.BooleanField(default=False)
    staff_task          = models.CharField(max_length=1, blank=True, null=True)
    rol                 = models.CharField(max_length=1, choices=choices.ROL_CHOICES, blank=True, null=True, verbose_name="Rol")
    food                = models.CharField(max_length=1, choices=choices.FOOD_CHOICES, blank=True, null=True, verbose_name="Dieta")
    transportation      = models.CharField(max_length=1, choices=choices.TRANSPORTATION_CHOICES, blank=True, null=True, verbose_name="Transporte")
    number_underage     = models.DecimalField(max_digits=1, decimal_places=0, null=True, verbose_name="Hijxs")
    arrival_date        = models.DateField(blank=True, null=True, verbose_name="Fecha de llegada")
    leave_date          = models.DateField(blank=True, null=True, verbose_name="Fecha de partida")
    inscription_date    = models.DateField(blank=True, null=True)
    cancelled           = models.BooleanField(default=True, verbose_name="cancelación")
    cession_user        = models.DecimalField(max_digits=5, decimal_places=0, null=True)
    cession_verification_id_organizater = models.DecimalField(max_digits=5, decimal_places=0, null=True)
    raffled             = models.BooleanField(default=False, verbose_name="sorteado")
    help_with           = models.CharField(max_length=1, choices=choices.HELP_WITH_CHOICES, blank=True, null=True, verbose_name="Coopera con:") # Choise ??
    extra_details       = models.CharField(max_length=255, blank=True, null=True, verbose_name="Detalles Extras")

class EventGroupManager(GroupManager):

    def save(self, name):
        group = Group.objects.get_or_create(name=name)[0]
        for perm in EventGroup_Perms:
            add_perm = Permission.objects.get(codename=perm)
            group.permissions.add(add_perm)
        return super(EventGroupManager, self)

class EventGroup(Group):
    """
        Create a proxy for class Group of django.contrib.auth.models
    """
    objects = EventGroupManager()

    class Meta:
        proxy = True

    def __str__(self):
        return "{}".format(self.name)
