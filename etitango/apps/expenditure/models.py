from django.db import models
from apps.events.models import Event
from apps.profiles.models import User

TYPE_CHOICES = (
('First', '1'),
('Second', '2'),
('Third', '3'),
('Fourth', '4')
)

class Expenditure(models.Model):
    # eti_event = models.ForeignKey(Event, on_delete=models.CASCADE, choices=ACTIVE_EVENT_CHOICES) #Tiene que estar atada a cada evento de ETI
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Evento') #El establecimiento que lo generó
    expendtype = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Tipo de gasto') #Rubro
    description = models.CharField(max_length=100,blank=False, verbose_name='Descripción') #Breve descripción del gasto: obligatoria
    detail = models.TextField(blank=False, verbose_name='Detalle') #Detalle del gasto: obligatorio
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Precio/Costo')#Valor del gasto realizado
    state = models.BooleanField(null=True, verbose_name='Verificado') #Si fué o no verificada
    submitted = models.DateTimeField(auto_now_add=True) #Fecha en que se cargó el gasto: es automático
    receipt = models.ImageField(upload_to='receipt/', verbose_name='Recibo/Factura') #Imagen del recibo
        
    def __str__(self):
        return self.description

class ExpenditureLog(models.Model):
    #expenditure_id = models.ForeignKey(Expenditure, on_delete=models.CASCADE)
    #staff_id = models.ForeignKey(User, on_delete=models.CASCADE) #ID del usuario que lo modifico
    log_message = models.TextField(blank=False)
    entry_modification_date = models.DateTimeField() #Fecha de modificación de un campo.

    def __str__(self):
        return self.log_message
