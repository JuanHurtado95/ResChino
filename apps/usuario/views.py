from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FormularioLogin
from .forms import RegistroForm

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

from django.views.generic import CreateView, TemplateView

from django.contrib.auth.models import User

# Create your views here.
def Home(request):
    return render(request, 'home.html')


class Login(FormView):
    template_name = 'loginUser.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('principalUser')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('accounts/login/')


def principalUser(request):
    return render(request, 'principal.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = "register.html"
    form_class = RegistroForm
    success_url = reverse_lazy('principalUser')

class pedido(TemplateView):
    template_name= 'pedido.html'


