from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.ExpenditureAdd.as_view(), name='expenditure_add'),
]