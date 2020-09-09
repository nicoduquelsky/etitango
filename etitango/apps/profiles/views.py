from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.forms import modelformset_factory, formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, TemplateView, View, UpdateView
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from six import StringIO # probably this will be fail in server

# #EMAIL CONFIRMATION
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives #EmailMessage
from django.template import Context
from django.template.loader import render_to_string

# APPS
from apps.countries.models import Country, Province, City
from apps.events.models import Event

# UTILS
from utils.defs import PanelContextMixin, PermissionContextMixin
from utils.tokens import account_activation_token
from utils.image_utils import reduce_image_size

# FORMS RENDERING
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, ButtonHolder

# SELF
from .forms import RegisterForm, UserForm, ProfileForm, PhotoForm, GroupMembersForm
from .models import User, Profile

# CONTANTS
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'
User = get_user_model()

## REGISTER;
def register_page(request):
    """
    TO DO: Rewrite it as Class View
    """
    User_form       = RegisterForm(request.POST or None)
    form            = ProfileForm(request.POST or None)
    context = {
        "form": User_form,
        "porm": form,
    }
    if User_form.is_valid() and form.is_valid():
        user = User_form.save(commit=False)
        user.save()
        form.instance.dni_type        = form.cleaned_data.get('dni_type').upper()
        form.instance.dni_number      = form.cleaned_data.get('dni_number').upper()
        form.instance.name            = form.cleaned_data.get('name').upper()
        form.instance.last_name       = form.cleaned_data.get('last_name').upper()
        form.instance.gender          = form.cleaned_data.get('gender').upper()
        form.instance.birth_date      = form.cleaned_data.get('birth_date')
        form.instance.country_id      = form.cleaned_data.get('country')
        form.instance.province_id     = form.cleaned_data.get('province')
        form.instance.city_id         = form.cleaned_data.get('city')
        user.profile = form.instance
        user.profile.save()
        # EMAIL VALIDATION:
        current_site = get_current_site(request)
        context = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            }
        c = Context(context)

        text_content = render_to_string('registration/acc_active_email.txt', context)
        html_content = render_to_string('registration/acc_active_email.html', context)
        mail_subject = 'Activa tu cuenta'
        email = EmailMultiAlternatives(mail_subject, text_content)
        email.attach_alternative(html_content, "text/html")
        to_email = User_form.cleaned_data.get('email')
        email.to = [to_email]
        email.send()
        messages.add_message(request, messages.INFO, User_form.cleaned_data['email'])
        return redirect('register_done')

    else:
        form = RegisterForm()
    return render(request, 'registration/register_form.html', context )

class register_done_page(View):
    def get(self, request):
        storage = messages.get_messages(request)
        for message in storage:
            name = message
            break
        return render(request, "registration/register_done.html", {'message':message })

## EMAIL CONFIRMATION
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, "registration/register_confirm.html", {})
    else:
        return render(request, "registration/register_confirm.html", {})

# CLASSES

## PROFILES
class view_profile_page(PanelContextMixin, TemplateView):
    model           = Profile
    success_url     = reverse_lazy('profile')
    template_name   = 'profiles/profile_view.html'
    title           =  _("Welcome, ")

class edit_profile_page(PanelContextMixin, UpdateView):
    model           = Profile
    form_class      = ProfileForm
    template_name   = 'profiles/profile_edit_form.html'
    title           =  _("Edit your Profile")
    success_url     = reverse_lazy('profile')
    success_message = 'Tu perfil fue actualizado con exito!'

    def get_object(self, queryset=None):
        return self.request.user.profile


    def form_valid(self, form):
        form.instance.dni_type      = form.cleaned_data.get('dni_type').upper()
        form.instance.dni_number    = form.cleaned_data.get('dni_number').upper()
        form.instance.name          = form.cleaned_data.get('name').upper()
        form.instance.last_name     = form.cleaned_data.get('last_name').upper()
        form.instance.gender        = form.cleaned_data.get('gender').upper()
        form.instance.birth_date    = form.cleaned_data.get('birth_date')
        form.instance.country_id    = form.cleaned_data.get('country')
        form.instance.province_id   = form.cleaned_data.get('province')
        form.instance.city_id       = form.cleaned_data.get('city')
        form.instance.update = True
        form.instance.email = self.request.user
        # Avatar is conserved
        form.instance.avatar = Profile.objects.get(email=form.instance.email).avatar
        form.save()
        return super(edit_profile_page, self).form_valid(form)

class edit_photo_page(PanelContextMixin, UpdateView):
    model           = Profile
    form_class      = PhotoForm
    template_name   = 'profiles/profile_edit_photo_form.html'
    success_url     = reverse_lazy('profile')

    def get_object(self, queryset=None):
       return self.request.user.profile

    def post(self, request, *args, **kwargs):
        form = PhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            old_avatar = self.get_object().avatar
            # delete old file
            old_avatar.delete(False)
            # use form.cleaned_data.get('avatar')
            avatar = reduce_image_size(form.cleaned_data.get('avatar'), new_size=(150, 150))
            form.instance.profile.avatar = avatar
            form.save()
            return super(edit_photo_page, self).form_valid(form)

# GROUP
class edit_group_page(PanelContextMixin, PermissionContextMixin, FormView):
    permission_required = ('events.add_eventgroup',)
    model = Profile
    form_class = formset_factory(form=GroupMembersForm, extra=2)
    success_url = reverse_lazy('profile')
    template_name = "groups/create_group_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        helper = GroupMembersFormSetHelper()
        helper.form_show_labels = False         # For manually render <form> tags on template
        #helper.add_input(Submit('submit', 'Confirmar'))    # Uncomment if form_show_labels = True
        helper.form_tag = False
        context['helper'] = helper
        return context

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        user = self.request.user
        form = GroupMembersForm(self.request.POST)
        if form.is_valid():
            _group = Event.objects.get(staff_id=user).group
            _member = User.objects.get(email=form.cleaned_data.get('members'))
            _member.groups.add(_group)
            return super(edit_group_page, self).form_valid(form)

# CRISPY FORMS RENDERING
class GroupMembersFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            'members',
        )