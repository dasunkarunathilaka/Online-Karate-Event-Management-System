from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from views import genericUser, slkf, district, province, association

urlpatterns = [
    url(r'^$', genericUser.index, name='index'),
    # Don't need as_view() function call because index is a function, not a class.
    # Home page directives.
    url(r'^tournament-page$', genericUser.tournamentPage, name='tournament-page'),

    # User auth urls
    url(r'^accounts', include('django.contrib.auth.urls')),

    # This directs to a html page with buttons to choose which type of user to create.
    url(r'^accounts/signup$', slkf.SignUpDirectingView.as_view(), name='signup'),

    # User creation urls.
    url(r'^accounts/signup/slkf$', slkf.SlkfSignUpView.as_view(), name='slkf_signup'),
    url(r'^accounts/signup/association$', association.AssociationSignUpView.as_view(), name='association_signup'),
    url(r'^accounts/signup/district$', district.DistrictSignUpView.as_view(), name='district_signup'),
    url(r'^accounts/signup/province$', province.ProvinceSignUpView.as_view(), name='province_signup'),

    # Login urls.
    url(r'^accounts/login$', genericUser.customLogin, name='login'),
    url(r'^accounts/auth$', genericUser.userAuth, name='auth'),
    url(r'^accounts/logout$', genericUser.logout, name='logout'),

    # User portals.
    url(r'^slkf-portal$', slkf.SlkfPortal.as_view(), name='slkf-portal'),
    url(r'^association-portal$', association.AssociationPortal.as_view(), name='association-portal'),
    url(r'^district-portal$', district.DistrictPortal.as_view(), name='district-portal'),
    url(r'^province-portal$', province.ProvincePortal.as_view(), name='province-portal'),

    # Event urls
    # Create new event - done by the SLKF.
    url(r'^slkf-portal/create-event$', slkf.EventCreationView.as_view(), name='create-event'),

    # Opening/closing tournaments by SLKF
    url(r'^slkf-portal/open-tournament$', slkf.OpenTournament.as_view(), name='open-tournament'),
    url(r'^slkf-portal/close-tournament$', slkf.CloseTournament.as_view(), name='close-tournament'),

    # Association functions
    # Player Registration
    url(r'^association-portal/player-registration$', association.PlayerRegistrationView.as_view(),
        name='player-registration'),
    url(r'^association-portal/player-registered$',
        TemplateView.as_view(template_name='event-management-system/association/playerRegistrationSuccess.html')),

    # Coach Registration
    url(r'^association-portal/coach-registration$', association.CoachRegistrationView.as_view(),
        name='coach-registration'),

    # View registered players/coaches
    url(r'^association-portal/view-players$', association.RegisteredPlayerListView.as_view(),
        name='view-players'),
    url(r'^association-portal/view-coaches$', association.RegisteredCoachListView.as_view(),
        name='view-coaches'),

    # View draws
    url(r'^association-portal/display-all-events-draws-for-association$', association.EventsListViewForDraws.as_view(),
        name='all-events-draws-for-association'),

    # Display players on events as a List before shuffling.
    url(r'^association-portal/display-all-events-draws-for-association/draws/$',
        association.PlayersListByEventViewBeforeShuffle.as_view(),
        name='view-players-on-events-draws-for-association'),

    # SLKF functions
    url(r'^slkf-portal/display-all-events-player$', slkf.EventsListViewForEvents.as_view(), name='all-events-players'),
    url(r'^slkf-portal/display-all-events-draws$', slkf.EventsListViewForDraws.as_view(), name='all-events-draws'),
    url(r'^slkf-portal/display-associations$', slkf.AssociationsListView.as_view(), name='association-list'),
    url(r'^slkf-portal/view-users$',
        TemplateView.as_view(template_name='event-management-system/slkf/userListDirect.html'), name='view-users'),
    url(r'^slkf-portal/tournament-options$',
        TemplateView.as_view(template_name='event-management-system/slkf/tournamentOptions.html'), name='tournament-options'),

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
    url(r'^slkf-portal/display-all-events-players/players/$', slkf.PlayersListByEventView.as_view(),
        name='view-players-on-events-players'),

    # Display players on events as a List before shuffling.
    url(r'^slkf-portal/display-all-events-draws/draws/$', slkf.PlayersListByEventViewBeforeShuffle.as_view(),
        name='view-players-on-events-draws'),

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

    # District Functions
    url(r'^district-portal/view-events/$', district.DistrictEventsListView.as_view(),
        name='district-events'),
    url(r'^district-portal/view-players/$', district.DistrictPlayersListView.as_view(),
        name='district-players'),
    url(r'^district-portal/view-coaches/$', district.DistrictCoachesListView.as_view(),
        name='district-coaches'),
    url(r'^district-portal/view-events/display-events/players/$', district.DistrictPlayersByEventListView.as_view(),
        name='view-dis-players-on-events'),

    # Province Functions
    url(r'^province-portal/view-players/$', province.ProvincePlayersListView.as_view(),
        name='province-players'),
    url(r'^province-portal/view-events/$', province.ProvinceEventsListView.as_view(),
        name='province-events'),
    url(r'^province-portal/view-coaches/$', province.ProvinceCoachesListView.as_view(),
        name='province-coaches'),
    url(r'^province-portal/view-events/display-events/players/$', province.ProvincePlayersByEventListView.as_view(),
        name='view-prov-players-on-events'),

    # Generic User Functions
    url(r'^tournament-page/view-events$', genericUser.EventsListView.as_view(), name='view-events'),
    url(r'^tournament-page/view-associations$', genericUser.AssociationsListView.as_view(), name='view-associations'),

]
