from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration',views.registration,name='registration'),
    path('login/',auth_views.LoginView.as_view(template_name='default/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='default/logout.html'),name='logout'),
    #services
    path('askService/',views.ask_service,name='askService')   , 
    path('profile/',views.profile,name='profile')    
]