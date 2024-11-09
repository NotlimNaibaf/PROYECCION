from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from datos.forms import RegistroUsuarioForm
from datos.models import Datos


class ListaDatoView(LoginRequiredMixin, ListView):
    model = Datos
    template_name = 'proyecciones/pesos_granja.html'

    context_object_name = 'datos'

    class ListaDatoView(LoginRequiredMixin, View):
        model = Datos
        template_name = 'proyecciones/pesos_granja.html'
        data = {}
        context_object_name = 'datos'

        def get_queryset(self):
            error = 0/0
            if self.request.user.rol == 'admin':
                return Datos.objects.all()

            return Datos.objects.filter(estado=True)

        def post(self, request):
            error = 0 / 0
            if request.user.rol == 'admin':
                self.data = {
                    "Datos": Datos.objects.all(),
                    "proyecciones": {}
                }

            return render(request, self.template_name, self.data)


class DetalleDatoView(LoginRequiredMixin, DetailView):
    model = Datos
    template_name = 'proyecciones/graficos.html'
    context_object_name = 'datos'



class CustomLoginView(LoginView):
    template_name = 'registro/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos. Por favor, ingrese nuevamente.')
        return super().form_invalid(form)

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Sesión cerrada correctamente.')
        response = redirect('login')
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response



class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registro/registro.html'
    success_url = reverse_lazy('pesos_granja')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, "Se ha registrado exitosamente.")
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)