from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='edit_profile'),
    path('profile/edit/photo/', views.ProfileEditPhotoView.as_view(), name='edit_photo'),
]