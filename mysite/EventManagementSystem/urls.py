from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from views import genericUser, slkf, district, province, association

urlpatterns = [
    url(r'^$', genericUser.index, name='index'),
    # url(r'^login$', views.login, name='login')

    # User auth urls

    url(r'^accounts', include('django.contrib.auth.urls')),

    # This directs to a html page with buttons to choose which type of user to create.
    url(r'^accounts/signup$', slkf.SignUpDirectingView.as_view(), name='signup'),

    # User creation urls.
    url(r'^accounts/signup/slkf$', slkf.SlkfSignUpView.as_view(), name='slkf_signup'),
    url(r'^accounts/signup/association$', association.AssociationSignUpView.as_view(), name='association_signup'),
    url(r'^accounts/signup/district$', district.DistrictSignUpView.as_view(), name='district_signup'),
    url(r'^accounts/signup/province$', province.ProvinceSignUpView.as_view(), name='province_signup'),

    url(r'^accounts/signup/signup-success$', genericUser.signupSuccess, name='signup-success'),

    # Login urls.
    url(r'^accounts/login$', genericUser.customLogin, name='login'),
    url(r'^accounts/auth$', genericUser.userAuth, name='auth'),
    url(r'^accounts/loggedin$', genericUser.loggedin, name='loggedin'),
    url(r'^accounts/logout$', genericUser.logout, name='logout'),
    url(r'^accounts/invalid$', genericUser.invalidLogin, name='invalid'),

    # User portals.
    url(r'^slkf-portal$', slkf.SlkfPortal.as_view(), name='slkf-portal'),
    url(r'^association-portal$', association.AssociationPortal.as_view(), name='association-portal'),
    # url(r'^district-portal', district.DistrictPortal.as_view(), name='district-portal'),
    # url(r'^province-portal', province.ProvincePortal.as_view(), name='province-portal'),

    # Event urls
    # Create new event - done by the SLKF.
    url(r'^slkf-portal/create-event$', slkf.EventCreationView.as_view(), name='create-event'),
    url(r'^slkf-portal/event-created$',
        TemplateView.as_view(template_name='event-management-system/slkf/eventCreated.html')),

    # Association functions
    # Player Registration
    url(r'^association-portal/player-registration$', association.PlayerRegistrationView.as_view(),
        name='player-registration'),
    url(r'^association-portal/player-registered$',
        TemplateView.as_view(template_name='event-management-system/association/playerRegistrationSuccess.html')),

    # Coach Registration
    url(r'^association-portal/coach-registration$', association.CoachRegistrationView.as_view(),
        name='coach-registration'),
    url(r'^association-portal/coach-registered$',
        TemplateView.as_view(template_name='event-management-system/association/coachRegistrationSuccess.html')),

    # View registered players/coaches
    url(r'^association-portal/view-players$', association.RegisteredPlayerListView.as_view(),
        name='view-players'),
    url(r'^association-portal/view-coaches$', association.RegisteredCoachListView.as_view(),
        name='view-coaches'),

    # SLKF functions
    url(r'^slkf-portal/display-all-events$', slkf.EventsListView.as_view(), name='all-events'),
    url(r'^slkf-portal/display-associations$', slkf.AssociationsListView.as_view(), name='association-list'),
    url(r'^slkf-portal/view-users$',
        TemplateView.as_view(template_name='event-management-system/slkf/userListDirect.html'), name='view-users'),

    url(r'^slkf-portal/view-users/display-slkf-users$', slkf.SlkfUsersListView.as_view(), name='slkf-users'),
    url(r'^slkf-portal/view-users/display-district-users$', slkf.DistrictUsersListView.as_view(),
        name='district-users'),
    url(r'^slkf-portal/view-users/display-province-users$', slkf.ProvinceUsersListView.as_view(),
        name='province-users'),

    url(r'^slkf-portal/display-associations/players/$', slkf.PlayersListByAssociationView.as_view(),
        name='slkf-player-list'),
    url(r'^slkf-portal/display-associations/coaches/$', slkf.RegisteredCoachSlkfListView.as_view(),
        name='slkf-coach-list'),

    # Display all registered players
    url(r'^slkf-portal/view-players/$', slkf.AllPlayersListView.as_view(),
        name='view-all-players'),

    # Display players on events.
    url(r'^slkf-portal/display-all-events/players/$', slkf.PlayersListByEventView.as_view(),
        name='view-players-on-events'),

    # Display players on districts.
    url(r'^slkf-portal/view-users/display-district-users/players/$', slkf.PlayersListByDistrictView.as_view(),
        name='view-players-on-districts'),

    # Display players on provinces.
    url(r'^slkf-portal/view-users/display-province-users/players/$', slkf.PlayersListByProvinceView.as_view(),
        name='view-players-on-provinces'),

    # User profile options
    url(r'^profile$',
        TemplateView.as_view(template_name='event-management-system/user-profile/userProfile.html'),
        name='user-profile'),
    url(r'^user-profile/change-password$', 'django.contrib.auth.views.password_change',
        {'template_name': 'event-management-system/user-profile/resetPassword.html'},
        name='reset-password'),

    # Password reset urls.
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]
