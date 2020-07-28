from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenditure_up, name='expenditure_up'),
]