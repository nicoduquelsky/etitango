from django.db import models
from django.contrib.auth.models import User

class Expenditure(models.Model):
    expenditure = models.CharField(max_length=100)
    description = models.TextField()
    submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)