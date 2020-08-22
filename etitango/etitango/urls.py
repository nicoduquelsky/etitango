from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls import url
#from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

#For displaying media and static files
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# APPS
from apps.pages import views as pages
from apps.profiles import views as profiles
from apps.events import views as events
from apps.blog import views as blog
from apps.countries import views as countrie


#CREATE BOSS AND REVIEW GROPUPS
from utils.perms import Create_SuperGroups, BossGroup_Perms, ReviewGroup_Perms

urlpatterns = [
    # TOKENS
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        profiles.activate, name='activate'),

    # AJAX
    # path('ajax/load-provinces/', countries.load_provinces, name='ajax_load_provinces'),
    # path('ajax/load-cities/', countries.load_cities, name='ajax_load_cities'),

    # PATHS
    path('', pages.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('historia', pages.HistoriaView.as_view(), name='historia'),
    path('manifiesto', pages.ManifiestoView.as_view(), name='manifiesto'),
    path('protocolo', pages.ProtocoloView.as_view(), name='protocolo'),

    ## PROFILES
    url('^', include('django.contrib.auth.urls')),
    path('register/done/', profiles.register_done_page.as_view(), name='register_done'),
    path('register/', profiles.register_page, name='register'),
    path('accounts/profile/', profiles.view_profile_page.as_view(), name='profile'),
    path('accounts/profile/edit/', profiles.edit_profile_page.as_view(), name='edit_profile'),
    path('accounts/profile/edit/photo/', profiles.edit_photo_page.as_view(), name='edit_photo'),

    ## EVENTS
    path('event/create/', events.create_event_page.as_view(), name='create_event'),
    path('event/edit/', events.edit_event_page.as_view(), name='edit_event'),
    path('event/active/', events.active_event_page.as_view(), name='active_event'),
    path('event/active/done/', events.done_active_event_page.as_view(), name='active_event_done'),
    path('event/view/', events.view_event_page.as_view(), name='view_event'),
    path('event/done/', events.done_event_page.as_view(), name='event_done'),
    path('blog/', blog.BlogView.as_view(), name='blog'),

    ## INSCRIPTIONS
    path('event/inscription/', events.new_inscription_page.as_view(), name='new_inscription'),
    path('event/inscription/done/', events.inscription_done_page.as_view(), name='inscription_done'),

    ## GROUPS
    path('event/group/edit/', profiles.edit_group_page.as_view(), name='edit_group'),

    ##EXPENDITURE
    path('expenditure/', include('apps.expenditure.urls')),

] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Create_SuperGroups()