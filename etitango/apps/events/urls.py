from django.urls import path
from . import views
from apps.profiles.views import GroupEditView

urlpatterns = [
    path('create/', views.CreateEventView.as_view(), name='create_event'),
    path('edit/', views.EditEventView.as_view(), name='edit_event'),
    path('active/', views.ActiveEventView.as_view(), name='active_event'),
    path('active/done/', views.ActiveEventDoneView.as_view(), name='active_event_done'),
    path('view/', views.EventView.as_view(), name='view_event'),
    path('done/', views.EventDoneView.as_view(), name='event_done'),
]

## INSCRIPTIONS
urlpatterns += [
    path('inscription/', views.InscriptionView.as_view(), name='new_inscription'),
    path('inscription/done/', views.InscriptionDoneView.as_view(), name='inscription_done'),
]

## GROUPS
urlpatterns += [
    path('group/edit/', GroupEditView.as_view(), name='edit_group'),
]