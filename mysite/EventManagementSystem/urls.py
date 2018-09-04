from django.conf.urls import url
from views import genericUser

urlpatterns = [
    url(r'^$', genericUser.index, name='index'),
    # url(r'^login$', views.login, name='login')

    # User auth urls
    # url(r'^login$', views.customLogin, name='login'),
    # url(r'^auth$', views.userAuth, name='auth'),
    # url(r'^logged-in', views.loggedin, name='loggedin'),
    # url(r'^logout$', views.logout, name='logout'),
    # url(r'^invalid$', views.invalidLogin, name='invalid'),

    # User creation can only be done by the SLKF and super admin.
    # url(r'^create-user', views.signupUser, name='signup'),
    # url(r'^signed-up$', views.signupSuccess, name='signedup'),

]
