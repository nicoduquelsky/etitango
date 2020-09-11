from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView, View, UpdateView
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from six import StringIO  # probably this will be fail in server

# #EMAIL CONFIRMATION
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives  # EmailMessage
from django.template import Context
from django.template.loader import render_to_string

# APPS
from apps.countries.models import Country, Province, City
from apps.events.models import Event

# UTILS
from utils.defs import PanelContextMixin, PermissionContextMixin
from utils.tokens import account_activation_token
from utils.image_utils import reduce_image_size
from utils.widgets import check_recaptcha

# SELF
from .forms import RegisterForm, UserForm, ProfileForm, PhotoForm, GroupMembersForm
from .models import User, Profile

# CONTANTS
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'
User = get_user_model()

# REGISTER


@check_recaptcha
def register_page(request):
    """
    TO DO: Rewrite it as Class View
    """

    user_form = RegisterForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "public_key": settings.GOOOGLE_RECAPTCHA_PUBLIC_KEY,
    }
    if user_form.is_valid() and profile_form.is_valid() and request.recaptcha_is_valid:
        profile_form.instance.dni_type = profile_form.cleaned_data.get(
            'dni_type').upper()
        profile_form.instance.dni_number = profile_form.cleaned_data.get(
            'dni_number').upper()
        profile_form.instance.name = profile_form.cleaned_data.get(
            'name').upper()
        profile_form.instance.last_name = profile_form.cleaned_data.get(
            'last_name').upper()
        profile_form.instance.gender = profile_form.cleaned_data.get(
            'gender').upper()
        profile_form.instance.birth_date = profile_form.cleaned_data.get(
            'birth_date')
        profile_form.instance.country_id = profile_form.cleaned_data.get(
            'country')
        profile_form.instance.province_id = profile_form.cleaned_data.get(
            'province')
        profile_form.instance.city_id = profile_form.cleaned_data.get('city')
        user = user_form.save(commit=False)
        user.save()
        user.profile = profile_form.instance
        user.profile.save()

        # EMAIL VALIDATION
        current_site = get_current_site(request)
        mail_data = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        }

        text_content = render_to_string(
            'registration/acc_active_email.txt', mail_data)
        html_content = render_to_string(
            'registration/acc_active_email.html', mail_data)
        mail_subject = 'Activa tu cuenta'
        email = EmailMultiAlternatives(mail_subject, text_content)
        email.attach_alternative(html_content, "text/html")
        to_email = user_form.cleaned_data.get('email')
        email.to = [to_email]
        email.send()
        messages.add_message(request, messages.INFO,
                             user_form.cleaned_data['email'])
        return redirect('register_done')

    else:
        form = RegisterForm()

    return render(request, 'registration/register_form.html', context)


class register_done_page(View):

    def get(self, request):

        storage = messages.get_messages(request)
        for message in storage:
            name = message
            break
        return render(request, "registration/register_done.html", {'message': message})

# EMAIL CONFIRMATION


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


class view_profile_page(PanelContextMixin, TemplateView):

    model = Profile
    success_url = reverse_lazy('profile')
    template_name = 'profiles/profile_view.html'
    title = _("Welcome, ")


class edit_profile_page(PanelContextMixin, UpdateView):

    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_edit_form.html'
    title = _("Edit your Profile")
    success_url = reverse_lazy('profile')
    success_message = 'Tu perfil fue actualizado con exito!'

    @method_decorator(check_recaptcha)
    def dispatch(self, *args, **kwargs):

        return super().dispatch(*args, **kwargs)

    def get_object(self, queryset=None):

        return self.request.user.profile

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)
        context["public_key"] = settings.GOOOGLE_RECAPTCHA_PUBLIC_KEY
        return context

    def form_valid(self, form):

        if self.request.recaptcha_is_valid:
            form.instance.dni_type = form.cleaned_data.get('dni_type').upper()
            form.instance.dni_number = form.cleaned_data.get(
                'dni_number').upper()
            form.instance.name = form.cleaned_data.get('name').upper()
            form.instance.last_name = form.cleaned_data.get(
                'last_name').upper()
            form.instance.gender = form.cleaned_data.get('gender').upper()
            form.instance.birth_date = form.cleaned_data.get('birth_date')
            form.instance.country_id = form.cleaned_data.get('country')
            form.instance.province_id = form.cleaned_data.get('province')
            form.instance.city_id = form.cleaned_data.get('city')
            form.instance.update = True
            form.instance.email = self.request.user
            # Avatar is conserved
            form.instance.avatar = Profile.objects.get(
                email=form.instance.email).avatar
            form.save()
            messages.success(self.request, _('¡Su perfil fue actualizado con exito!'))
            return super(edit_profile_page, self).form_valid(form)

        else:
            return self.form_invalid(form)


class edit_photo_page(PanelContextMixin, UpdateView):

    model = Profile
    form_class = PhotoForm
    template_name = 'profiles/profile_edit_photo_form.html'
    success_url = reverse_lazy('profile')

    @method_decorator(check_recaptcha)
    def dispatch(self, *args, **kwargs):

        return super().dispatch(*args, **kwargs)

    def get_object(self, queryset=None):

        return self.request.user.profile

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)
        context["public_key"] = settings.GOOOGLE_RECAPTCHA_PUBLIC_KEY
        return context

    def form_valid(self, form):

        if self.request.recaptcha_is_valid:
            # delete old file
            old_avatar = self.get_object().avatar
            old_avatar.delete(False)
            avatar = reduce_image_size(
                form.cleaned_data.get('avatar'), new_size=(150, 150))
            form.instance.profile.avatar = avatar
            form.save()
            messages.success(self.request, _('¡La foto de su perfil fue actualizado con exito!'))
            return super(edit_photo_page, self).form_valid(form)
        else:
            return super(edit_photo_page, self).form_invalid(form)


class edit_group_page(PanelContextMixin, PermissionContextMixin, FormView):

    permission_required = ('events.add_eventgroup',)
    model = Profile
    # formset will be useful for a allow to assign few members to the same Evengroup
    form_class = formset_factory(Profile, formset=GroupMembersForm, extra=2)
    success_url = reverse_lazy('profile')
    template_name = "groups/create_group_form.html"

    def post(self, *args, **kwargs):

        super().post(*args, **kwargs)
        """
            Save each new member
        """
        user = self.request.user
        form = GroupMembersForm(self.request.POST)
        if form.is_valid():
            _group = Event.objects.get(staff_id=user).group
            _member = User.objects.get(email=form.cleaned_data.get('members'))
            _member.groups.add(_group)
            messages.success(self.request, _('¡Su grupo fue actualizado con exito!'))
            return super(edit_group_page, self).form_valid(form)
