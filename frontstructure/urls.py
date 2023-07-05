from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup_views, name='signup'),
    path('login/', views.login_views, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]