from django.urls import path
from .views import (
    RegistroUsuarioView, CustomLoginView, ListaDatoView, DetalleDatoView, CustomLogoutView)

urlpatterns = [
    path('', ListaDatoView.as_view(), name='pesos_granja'),

    path('registro/', RegistroUsuarioView.as_view(), name='registro'),

    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('proyecciones/<int:pk>/', DetalleDatoView.as_view(), name='graficos'),


   ]