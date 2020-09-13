from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.ExpenditureUp.as_view(), name='expenditure_up'),
]