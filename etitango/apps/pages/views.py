# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# APPS
from utils.defs import EventContextMixin

# Home.
class HomeView(EventContextMixin, LoginView):
    template_name = 'home.html'

class HistoryView(EventContextMixin, LoginView):
    template_name =  "history.html"

class ProtocolView(EventContextMixin, LoginView):
    template_name = "protocol.html"

class ManifestView(EventContextMixin, LoginView):
    template_name = "manifiest.html"
