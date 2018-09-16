from django.conf.urls import url, include
from views import genericUser, slkf, district, province, association

urlpatterns = [
    url(r'^$', genericUser.index, name='index'),
    # url(r'^login$', views.login, name='login')

    # User auth urls

    url(r'^accounts', include('django.contrib.auth.urls')),

    url(r'^accounts/signup$', slkf.SignUpDirectingView.as_view(), name='signup'),
    # This directs to a html page with buttons to choose which type of user to create.

    url(r'^accounts/signup/slkf$', slkf.SlkfSignUpView.as_view(), name='slkf_signup'),
    url(r'^accounts/signup/association$', association.AssociationSignUpView.as_view(), name='association_signup'),
    url(r'^accounts/signup/district$', district.DistrictSignUpView.as_view(), name='district_signup'),
    url(r'^accounts/signup/province', province.ProvinceSignUpView.as_view(), name='province_signup'),

    # url(r'^login$', views.customLogin, name='login'),
    # url(r'^auth$', views.userAuth, name='auth'),
    # url(r'^logged-in', views.loggedin, name='loggedin'),
    # url(r'^logout$', views.logout, name='logout'),
    # url(r'^invalid$', views.invalidLogin, name='invalid'),

    # User creation can only be done by the SLKF and super admin.
    # url(r'^create-user', views.signupUser, name='signup'),
    # url(r'^signed-up$', views.signupSuccess, name='signedup'),

]
