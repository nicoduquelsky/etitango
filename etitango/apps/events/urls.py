from django.urls import path
from . import views
from apps.profiles.views import edit_group_page

urlpatterns = [
    path('create/', views.create_event_page.as_view(), name='create_event'),
    path('edit/', views.edit_event_page.as_view(), name='edit_event'),
    path('active/', views.active_event_page.as_view(), name='active_event'),
    path('active/done/', views.done_active_event_page.as_view(), name='active_event_done'),
    path('view/', views.view_event_page.as_view(), name='view_event'),
    path('done/', views.done_event_page.as_view(), name='event_done'),
]

## INSCRIPTIONS
urlpatterns += [
    path('inscription/', views.new_inscription_page.as_view(), name='new_inscription'),
    path('inscription/done/', views.inscription_done_page.as_view(), name='inscription_done'),
]

## GROUPS
urlpatterns += [
    path('group/edit/', edit_group_page.as_view(), name='edit_group'),
]