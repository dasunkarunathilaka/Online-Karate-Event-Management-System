from django.urls import re_path, include
# from EventManagementSystem.views import genericUser
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from EventManagementSystem.views import genericUser as evG
# from .views import test_view as views

from .views import *

urlpatterns = [
    # re_path(r'^$', lambda request: HttpResponse("Hello World", content_type="text/plain")),
    re_path(r'^$', genericUser.index, None, 'index'),

    # User portals.
    re_path(r'^slkf-portal$', slkf.SlkfPortal.as_view(), None, 'slkf-portal'),
    re_path(r'^association-portal$', association.AssociationPortal.as_view(), None, 'association-portal'),
    re_path(r'^district-portal$', district.DistrictPortal.as_view(), None, 'district-portal'),
    re_path(r'^province-portal$', province.ProvincePortal.as_view(), None, 'province-portal'),

    re_path(r'^profile$',
            TemplateView.as_view(template_name='event-management-system/user-profile/userProfile.html'), None,
            'user-profile'),
    # re_path(r'^user-profile/change-password$', 'django.contrib.auth.views.password_change',
    #         {'template_name': 'event-management-system/user-profile/resetPassword.html'}, None,
    #         'reset-password'),

    # Password reset urls.
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(), None, 'password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordChangeDoneView.as_view(), None, 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(), None, 'password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), None, 'password_reset_complete'),

    # Login urls.
    re_path(r'^accounts/login$', genericUser.customLogin, None, 'login'),
    re_path(r'^accounts/auth$', genericUser.userAuth, None, 'auth'),
    re_path(r'^accounts/logout$', genericUser.logout, None, 'logout'),

    re_path(r'^tournament-page$', genericUser.tournamentPage, None, 'tournament-page'),

    ###########################################################################

    # User auth urls
    re_path(r'^accounts', include('django.contrib.auth.urls')),

    # This directs to a html page with buttons to choose which type of user to create.
    re_path(r'^accounts/signup$', slkf.SignUpDirectingView.as_view(), None, 'signup'),

    # User creation urls.
    re_path(r'^accounts/signup/slkf$', slkf.SlkfSignUpView.as_view(), None, 'slkf_signup'),
    # re_path(r'^accounts/signup/association$', association.AssociationSignUpView.as_view(), 'association_signup'),
    re_path(r'^accounts/signup/district$', district.DistrictSignUpView.as_view(), None, 'district_signup'),
    re_path(r'^accounts/signup/province$', province.ProvinceSignUpView.as_view(), None, 'province_signup'),

    # Login urls.
    re_path(r'^accounts/login$', genericUser.customLogin, None, 'login'),
    re_path(r'^accounts/auth$', genericUser.userAuth, None, 'auth'),
    re_path(r'^accounts/logout$', genericUser.logout, None, 'logout'),

    # User portals.
    re_path(r'^slkf-portal$', slkf.SlkfPortal.as_view(), None, 'slkf-portal'),
    re_path(r'^association-portal$', association.AssociationPortal.as_view(), None, 'association-portal'),
    re_path(r'^district-portal$', district.DistrictPortal.as_view(), None, 'district-portal'),
    re_path(r'^province-portal$', province.ProvincePortal.as_view(), None, 'province-portal'),

    # Event urls
    # Create new event - done by the SLKF.
    re_path(r'^slkf-portal/create-event$', slkf.EventCreationView.as_view(), None, 'create-event'),

    # Opening/closing tournaments by SLKF
    re_path(r'^slkf-portal/open-tournament$', slkf.OpenTournament.as_view(), None, 'open-tournament'),
    re_path(r'^slkf-portal/close-tournament$', slkf.CloseTournament.as_view(), None, 'close-tournament'),

    # Association functions
    # Player Registration
    re_path(r'^association-portal/player-registration$', association.PlayerRegistrationView.as_view(), None,
            'player-registration'),

    # TODO: Resolve this
    re_path(r'^association-portal/player-registered$',
            TemplateView.as_view(template_name='event-management-system/association/playerRegistrationSuccess.html')),

    # Coach Registration
    re_path(r'^association-portal/coach-registration$', association.CoachRegistrationView.as_view(), None,
            'coach-registration'),

    # View registered players/coaches
    re_path(r'^association-portal/view-players$', association.RegisteredPlayerListView.as_view(), None,
            'view-players'),
    re_path(r'^association-portal/view-coaches$', association.RegisteredCoachListView.as_view(), None,
            'view-coaches'),

    # View draws
    re_path(r'^association-portal/display-all-events-draws-for-association$',
            association.EventsListViewForDraws.as_view(),
            None,
            'all-events-draws-for-association'),

    # Display players on events as a List before shuffling.
    re_path(r'^association-portal/display-all-events-draws-for-association/draws/$',
            association.PlayersListByEventViewBeforeShuffle.as_view(), None,
            'view-players-on-events-draws-for-association'),

    # SLKF functions
    re_path(r'^slkf-portal/display-all-events-player$', slkf.EventsListViewForEvents.as_view(), None,
            'all-events-players'),
    re_path(r'^slkf-portal/display-all-events-draws$', slkf.EventsListViewForDraws.as_view(), None, 'all-events-draws'),
    re_path(r'^slkf-portal/display-associations$', slkf.AssociationsListView.as_view(), None, 'association-list'),
    re_path(r'^slkf-portal/view-users$',
            TemplateView.as_view(template_name='event-management-system/slkf/userListDirect.html'), None, 'view-users'),
    re_path(r'^slkf-portal/tournament-options$',
            TemplateView.as_view(template_name='event-management-system/slkf/tournamentOptions.html'), None,
            'tournament-options'),

    re_path(r'^slkf-portal/view-users/display-slkf-users$', slkf.SlkfUsersListView.as_view(), None, 'slkf-users'),
    re_path(r'^slkf-portal/view-users/display-district-users$', slkf.DistrictUsersListView.as_view(), None,
            'district-users'),
    re_path(r'^slkf-portal/view-users/display-province-users$', slkf.ProvinceUsersListView.as_view(), None,
            'province-users'),

    re_path(r'^slkf-portal/display-associations/players/$', slkf.PlayersListByAssociationView.as_view(), None,
            'slkf-player-list'),
    re_path(r'^slkf-portal/display-associations/coaches/$', slkf.RegisteredCoachSlkfListView.as_view(), None,
            'slkf-coach-list'),

    # Display all registered players
    re_path(r'^slkf-portal/view-players/$', slkf.AllPlayersListView.as_view(), None,
            'view-all-players'),

    # Display players on events.
    re_path(r'^slkf-portal/display-all-events-players/players/$', slkf.PlayersListByEventView.as_view(), None,
            'view-players-on-events-players'),

    # Display players on events as a List before shuffling.
    re_path(r'^slkf-portal/display-all-events-draws/draws/$', slkf.PlayersListByEventViewBeforeShuffle.as_view(), None,
            'view-players-on-events-draws'),

    # Display players on districts.
    re_path(r'^slkf-portal/view-users/display-district-users/players/$', slkf.PlayersListByDistrictView.as_view(), None,
            'view-players-on-districts'),

    # Display players on provinces.
    re_path(r'^slkf-portal/view-users/display-province-users/players/$', slkf.PlayersListByProvinceView.as_view(), None,
            'view-players-on-provinces'),


    # TODO: resolve this
    # re_path(r'^user-profile/change-password$', 'django.contrib.auth.views.password_change',
    #         {'template_name': 'event-management-system/user-profile/resetPassword.html'}, None,
    #         'reset-password'),
    #
    # # Password reset urls.
    # re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(), None, 'password_reset'),
    # re_path(r'^password_reset/done/$', auth_views.PasswordChangeDoneView.as_view(), None, 'password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         auth_views.PasswordResetConfirmView.as_view(), None, 'password_reset_confirm'),
    # re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), None, 'password_reset_complete'),

    # District Functions
    re_path(r'^district-portal/view-events/$', district.DistrictEventsListView.as_view(), None,
            'district-events'),
    re_path(r'^district-portal/view-players/$', district.DistrictPlayersListView.as_view(), None,
            'district-players'),
    re_path(r'^district-portal/view-coaches/$', district.DistrictCoachesListView.as_view(), None,
            'district-coaches'),
    re_path(r'^district-portal/view-events/display-events/players/$', district.DistrictPlayersByEventListView.as_view(),
            None,
            'view-dis-players-on-events'),

    # Province Functions
    re_path(r'^province-portal/view-players/$', province.ProvincePlayersListView.as_view(), None,
            'province-players'),
    re_path(r'^province-portal/view-events/$', province.ProvinceEventsListView.as_view(), None,
            'province-events'),
    re_path(r'^province-portal/view-coaches/$', province.ProvinceCoachesListView.as_view(), None,
            'province-coaches'),
    re_path(r'^province-portal/view-events/display-events/players/$', province.ProvincePlayersByEventListView.as_view(),
            None,
            'view-prov-players-on-events'),

    # Generic User Functions
    re_path(r'^tournament-page/view-events$', genericUser.EventsListView.as_view(), None, 'view-events'),
    re_path(r'^tournament-page/view-associations$', genericUser.AssociationsListView.as_view(), None,
            'view-associations'),

]
