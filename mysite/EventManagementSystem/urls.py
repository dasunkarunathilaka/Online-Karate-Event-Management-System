from django.conf.urls import url, include
from django.views.generic import TemplateView

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
    url(r'^accounts/signup/province', province.ProvinceSignUpView.as_view(), name='province_signup'),

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

    # Player Registration
    url(r'^association-portal/player-registration$', association.PlayerRegistrationView.as_view(),
        name='player-registration'),
    url(r'^association-portal/player-registered$',
        TemplateView.as_view(template_name='event-management-system/association/playerRegistrationSuccess.html')),

    # SLKF functions
    url(r'^slkf-portal/display-all-events$', slkf.EventsListView.as_view(), name='all-events'),
    url(r'^slkf-portal/display-associations$', slkf.AssociationsListView.as_view(), name='association-list'),
    url(r'^slkf-portal/view-users$',
        TemplateView.as_view(template_name='event-management-system/slkf/userListDirect.html'), name='view-users'),

    url(r'^slkf-portal/view-users/display-slkf-users$', slkf.SlkfUsersListView.as_view(), name='slkf-users'),
    url(r'^slkf-portal/view-users/display-district-users$', slkf.DistrictUsersListView.as_view(), name='district-users'),
    url(r'^slkf-portal/view-users/display-province-users$', slkf.ProvinceUsersListView.as_view(), name='province-users'),

]
