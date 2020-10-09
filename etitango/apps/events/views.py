from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View, UpdateView
from datetime import date

# UTILS
from utils.defs import PanelContextMixin, PermissionContextMixin

# SELF
from .forms import InscriptionForm, EventForm, EventActiveForm
from .models import Event, Inscription


# CLASSES

# EVENT
class CreateEventView(PanelContextMixin, PermissionContextMixin, FormView):
    # Only Boss Users can access.
    permission_required = ('events.add_event',)
    model = Event
    form_class = EventForm
    template_name = 'event_create.html'
    success_url = reverse_lazy('event_done')

    def form_valid(self, form):
        """
            Remember that in template level, we are only allowing to create
            a new event if there is no EventId linked to user
        """
        form.instance.staff = self.request.user
        # If User got a event linked, it only will update it.
        form.save()
        return super().form_valid(form)


class EditEventView(PanelContextMixin, PermissionContextMixin, FormView):
    # Only Boss Users can access.
    permission_required = ('events.change_event',)
    model = Event
    form_class = EventForm
    template_name = 'event_edit.html'
    success_url = reverse_lazy('event_done')

    # Template avoid the form if User dont get a event linked
    def form_valid(self, form):
        form.instance.staff_id = Event.objects.get(
            staff_id=self.request.user).staff_id
        form.save()
        return super().form_valid(form)


class ActiveEventView(PanelContextMixin, PermissionContextMixin, FormView):
    # Only Boss Users can access.
    permission_required = ('events.change_event',)
    model = Event
    form_class = EventActiveForm
    template_name = 'event_active.html'
    success_url = reverse_lazy('active_event_done')

    def post(self, request, *args, **kwargs):
        # TODO: Validate form
        form = EventActiveForm(request.POST)
        form.instance = Event.objects.get(staff_id=self.request.user)
        form.save()
        return super().form_valid(form)


class ActiveEventDoneView(PanelContextMixin, PermissionContextMixin, TemplateView):
    # Only Boss Users can access.
    permission_required = ('events.change_event',)
    template_name = 'event_active_done.html'
    title = ('Activation done')


class EventDoneView(PanelContextMixin, PermissionContextMixin, TemplateView):
    # Only Boss Users can access.
    permission_required = ('events.change_event',)
    template_name = 'event_done.html'
    title = ('Inscription done')


class EventView(PanelContextMixin, TemplateView):
    model = Event
    template_name = 'event_view.html'

# INSCRIPTION


class InscriptionView(PanelContextMixin, FormView):
    model = Inscription
    form_class = InscriptionForm
    template_name = 'new_inscription.html'
    success_url = reverse_lazy('inscription_done')

    def form_valid(self, form):
        # Need to be only one inscription per Event
        form.instance.inscription_date = date.today()
        form.instance.eti = Event.objects.get(
            active=True)  # only one eti must be active
        form.instance.email_id = self.request.user.id
        form.save()
        return super().form_valid(form)


class InscriptionDoneView(PanelContextMixin, TemplateView):
    template_name = 'inscription_done.html'
    title = ('Inscription done')
