"""RestauranteChino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.usuario.views import Login, Home, principalUser, RegistroUsuario, logoutUsuario, pedido
from apps.plato.views import Menu, show

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.plato.urls')),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('', Home, name='home'),
    path('menu/', show, name='menu'),
    path('principalUser/', login_required(principalUser), name='principalUser'),
    path('registro/', RegistroUsuario.as_view(), name='register'),
    path('pedido/', pedido.as_view(), name='pedido'),
]
