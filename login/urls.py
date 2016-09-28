from django.conf.urls import url
#from login.views import *
from . import views
 
urlpatterns = [
    url(r'^$', views.login, name='login'),
    #url(r'^authenticate/(?P<wsPort>[0-9]+)', views.authenticate, name='authenticate'),
    #url(r'^access/rejected/', views.rejected, name='rejected'),
    #url(r'^salir$', logout, {'next_page': '/'}),
    url(r'^loginUser/$', views.loginUser, name='loginUser'), 
    #url(r'^historial/$', views.getMakedGroup, name='getMakedGroup'),
]