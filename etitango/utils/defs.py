from django import forms
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms.models import model_to_dict
from datetime import date

# APPS
from apps.countries.models import Country, Province, City

from apps.events.models import Event

from apps.profiles.models import User, Profile

# CLASSES

class EventContextMixin(ContextMixin):
    """
        This Mixin is required for all views whith event information.
        PanelContextMixin inherit it, so avoid using it in views which user logged.

        Note: Was pulled apart specially for HomeView.
    """

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def EventActive(self, *args, **kwargs):
        try:
            event = Event.objects.get(active=True)
            return event
        except:
            return False

    def InscriptionOpen(self, *args, **kwargs):
        """
            Check which event is active and if its allowing inscriptions.
            + Back System accept multievents, but Front System can fail.
              So, only one event should be active at a time.
        """
        _date = date.today()
        try:
            event = self.EventActive()
            if event.open_date <= _date <= event.close_date:
                return event
            else:
                return False
        except:
            return False

    def GetEventId(self, *args, **kargs):
        """
            If user had created an event, is True.
            If True, it returns the event.object linked with the Boss User.
        """
        _event = False
        try:
            _event = Event.objects.get(staff=self.request.user)
            return _event
        except:
            return _event

    def GetGroupEventId(self, *args, **kwargs):
        """
            This function is not being used now, but will be useful.

            If user has created a Event, there should be a EventGroup created for.
            It returns the Event.Group linked with the Boss User,
            (which is the same of Group.object)
        """
        _group = False
        try:
            _group = Event.objects.get(staff=self.request.user).group
            return _group
        except:
            return _group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_active = self.EventActive()
        inscription_open = self.InscriptionOpen()
        context["EventId"] = self.GetEventId()
        context["GroupEventId"] = self.GetGroupEventId()
        context["EventActive"] = event_active
        context["EventOpen"] = inscription_open
        if event_active != False:
            context["boss"] = User.objects.get(id=event_active.staff_id)
        return context

class PanelContextMixin(LoginRequiredMixin, EventContextMixin):
    """
        This Mixin is required for all views which need an User logged.
    """
    extra_context = None

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return User.objects.filter(email=self.request.user.email).get()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["email"] = self.get_queryset
        return context

class EditorContextMixin(PermissionRequiredMixin):
    """
        This Mixin is required for editors views.
        Remember that boss users got this perm too (and many more),
        so they will pass this filter too.
    """

    permission_required = ("blog.can_edit",)

class ReviewContextMixin(PermissionRequiredMixin):
    """
        This Mixin is required for reviewers views.
    """

    permission_required = ("blog.confirm_payload",)

class PermissionContextMixin(PermissionRequiredMixin):
    """
        This Mixin is required for that views which are only allowed of Boss Users logged.
    """
    # Only bossGroup got the perms for change eventgroups
    permission_required = ('eventGroup.can_edit',)
