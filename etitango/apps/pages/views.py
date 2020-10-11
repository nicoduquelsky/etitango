# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# APPS
from utils.defs import EventContextMixin

# Home.
class HomeView(EventContextMixin, LoginView):
    template_name = '01_ETI_home.html'

class ErrorView(EventContextMixin, LoginView):
    template_name = '02_ETI_404.html'

class InProgressView(EventContextMixin, LoginView):
    template_name = '03_ETI_in_progress.html'

class AssemblyWaitView(EventContextMixin, LoginView):
    template_name = '04_ETI_assembly_wait.html'

class HistoryView(EventContextMixin, LoginView):
    template_name = '05_ETI_history.html'

class ComiteesView(EventContextMixin, LoginView):
    template_name = '06_ETI_comitees.html'

class GenderComiteeView(EventContextMixin, LoginView):
    template_name = '07_ETI_gender_comitee.html'

class GenderProtocolView(EventContextMixin, LoginView):
    template_name = '08_ETI_gender_protocol.html'

class GenderComiteeContactView(EventContextMixin, LoginView):
    template_name = '09_ETI_gender_comitee_contactus.html'

class LogInMailView(EventContextMixin, LoginView):
    template_name = '10_ETI_login_mail.html'

class LogInPasswordView(EventContextMixin, LoginView):
    template_name = '11_ETI_login_password.html'

