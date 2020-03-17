from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class FormularioLogin(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super(FormularioLogin, self)._init_(args,*kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email',
            ]
        labels = {
            'username': 'Nombre de usuario', 
            'first_name': 'Nombre', 
            'last_name': 'Apellidos', 
            'email': 'Correo',
        }