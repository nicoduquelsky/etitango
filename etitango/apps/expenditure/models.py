from django.db import models
#from PIL import Image
#from io import BytesIO
#from django.core.files import File
#from apps.events import Event
#from apps.profiles import User
from utils.image_utils import reduce_image_size

TYPE_CHOICES = (
('First', '1'),
('Second', '2'),
('Third', '3'),
('Fourth', '4')
)

class Expenditure(models.Model):
    #eti_event = models.ForeignKey(Event, on_delete=models.CASCADE) #Tiene que estar atada a cada evento de ETI
    owner = models.CharField(max_length=100) #El establecimiento que lo generó
    expendtype = models.CharField(max_length=30, choices=TYPE_CHOICES) #Rubro
    description = models.CharField(max_length=100,blank=False) #Breve descripción del gasto: obligatoria
    detail = models.TextField(blank=False) #Detalle del gasto: obligatorio
    price = models.DecimalField(max_digits=7, decimal_places=2)#Valor del gasto realizado
    state = models.BooleanField() #Si fué o no verificada
    submitted = models.DateTimeField(auto_now_add=True) #Fecha en que se cargó el gasto: es automático
    receipt = models.ImageField(upload_to='receipt/') #Imagen del recibo

    def save(self, *args, **kwargs):
        new_image = reduce_image_size(self.receipt, new_quality=90)

        self.receipt = new_image        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.description

class ExpenditureLog(models.Model):
    #expenditure_id = models.ForeignKey(Expenditure, on_delete=models.CASCADE)
    #staff_id = models.ForeignKey(User, on_delete=models.CASCADE) #ID del usuario que lo modifico
    log_message = models.TextField(blank=False)
    entry_modification_date = models.DateTimeField() #Fecha de modificación de un campo.

    def __str__(self):
        return self.log_message
