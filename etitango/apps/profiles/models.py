from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string

# ETITANGO
from etitango.settings import MEDIA_URL

# APPS
from apps.countries.models import City, Country, Province

# UTILS
from utils import choices

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("Debe ingresar una dirección de correo")
        if not password:
            raise ValueError("Debe ingresar una contraseña")

        user_obj    = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.is_staff  = is_staff
        user_obj.is_admin  = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True # Work like staff
        )
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email              = models.EmailField(max_length=255, unique=True)
    is_active          = models.BooleanField(default=False) # MUST BE FALSE. We active account after email confirmation.
    is_staff           = models.BooleanField(default=False) # PGP members could be staff in future
    is_admin           = models.BooleanField(default=False) # Same staff

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    def avatar_folder(request, *args, **kargs):
        path = ''.join(random.choice(string.ascii_letters) for x in range(16))
        path = "profiles/avatars/"+path+".png"
        return path

    email               = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    updated             = models.BooleanField(default=False) ## Useful for alert in profile panel
    name                = models.CharField(max_length=32, verbose_name="Nombre")
    last_name           = models.CharField(max_length=32, verbose_name="Apellido")
    dni_type            = models.CharField(max_length=4, choices=choices.DNI_TYPE_CHOICES, default='DNI', verbose_name="Tipo de Documento") # MULTIPASE :P
    dni_number          = models.CharField(max_length=11, unique=True, verbose_name="Numero de Documento") #  UNIQUE !! PASSSAPORT need CharField;
    birth_date          = models.DateField(blank=True, verbose_name="Fecha de Nacimiento", default="1900-1-1")   # Date, not DateTime.
    gender              = models.CharField(max_length=1, choices=choices.GENDER_CHOICES, verbose_name="Género")
    country             = models.ForeignKey(Country, on_delete=models.SET_NULL, to_field='country_id', null=True, verbose_name="País")
    province            = models.ForeignKey(Province, on_delete=models.SET_NULL, to_field='id', null=True, verbose_name="Provincia")
    city                = models.ForeignKey(City, on_delete=models.SET_NULL, to_field='id', null=True, verbose_name="ciudad")
    avatar              = models.ImageField(upload_to=avatar_folder, blank=True, default="profiles/avatar.jpg", verbose_name="Foto de Perfil")

    def get_full_name(self):
        return (self.last_name+" "+self.name)

    def get_short_name(self):
        return self.name

    @receiver(post_save, sender=User)
    # If a new User object is created, it will got assigned a profile instance too.
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(email=instance)

    @receiver(post_save, sender=User)
    # Save method is indepent of User, but response good if User is update.
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
