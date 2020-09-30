from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_profile_page.as_view(), name='profile'),
    path('profile/edit/', views.edit_profile_page.as_view(), name='edit_profile'),
    path('profile/edit/photo/', views.edit_photo_page.as_view(), name='edit_photo'),
]