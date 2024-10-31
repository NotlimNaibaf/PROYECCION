from django.contrib import admin
from django.urls import path, include

from datos import views
from datos.views import CustomLoginView, CustomLogoutView, DetalleDatoView, ListaDatoView, RegistroUsuarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datos.urls')),
    path('proyecciones/', ListaDatoView.as_view(), name='pesos_granja'),
    path('proyecciones/', DetalleDatoView.as_view(), name='graficos'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),

]
