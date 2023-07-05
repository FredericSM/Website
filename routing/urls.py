from django.urls import path
from . import views

urlpatterns = [
    path('routing/', views.routing_page, name='routing_page'),
]