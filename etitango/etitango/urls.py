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
from apps.countries import views as countries
from utils.perms import  EventGroup_Perms, BossGroup_Perms, Create_SuperGroups


urlpatterns = [
    # TOKENS
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        profiles.activate, name='activate'),

    # AJAX
    path('ajax/load-provinces/', countries.load_provinces,
         name='ajax_load_provinces'),
    path('ajax/load-cities/', countries.load_cities,
         name='ajax_load_cities'),

    ## PATHS
    path('', pages.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('error/', pages.ErrorView.as_view(), name='404'),
    path('in_progress/', pages.InProgressView.as_view(), name='in_progress'),
    path('assembly_wait/', pages.AssemblyWaitView.as_view(), name='assembly_wait'),
    path('history/', pages.HistoryView.as_view(), name='history'),
    path('comitees/', pages.ComiteesView.as_view(), name='comitees'),
    # path('comitees/', pages.AssemblyWaitView.as_view(), name='comitees'),
    path('gender_comitee/', pages.GenderComiteeView.as_view(), name='gender_comitee'),
    path('gender_protocol/', pages.GenderProtocolView.as_view(), name='gender_protocol'),
    path('gender_comitee_contactus/', pages.GenderComiteeContactView.as_view(), name='gender_comitee_contactus'),
    path('login_mail/', pages.LogInMailView.as_view(), name='login_mail'),
    path('login_password/', pages.LogInPasswordView.as_view(), name='login_password'),
    # path('login_password/', pages.AssemblyWaitView.as_view(), name='login_password'),

    ## PROFILES
    url('^', include('django.contrib.auth.urls')),
    path('register/done/', profiles.RegisterDoneView.as_view(), name='register_done'),
    # path('register/done/', pages.AssemblyWaitView.as_view(), name='register_done'),
    path('register/', profiles.register_page, name='register'),
    # path('register/', pages.AssemblyWaitView.as_view(), name='register'),
    path('accounts/', include('apps.profiles.urls')),

    ## EVENTS
    path('event/', include('apps.events.urls')),
    path('blog/', blog.BlogView.as_view(), name='blog'),

    ##EXPENDITURE
    path('expenditure/', include('apps.expenditure.urls')),

] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create_SuperGroups()