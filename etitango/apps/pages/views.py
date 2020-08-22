# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# APPS
from utils.defs import EventContextMixin

# Home.
class HomeView(EventContextMixin, LoginView):
    template_name = 'home.html'

class HistoriaView(EventContextMixin, LoginView):
    template_name =  "historia.html"

class ProtocoloView(EventContextMixin, LoginView):
    template_name = "protocolo_genero_ETI.html"

class ManifiestoView(EventContextMixin, LoginView):
    template_name = "manifiesto_etiano.html"
