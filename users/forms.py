from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

import re

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'exemplousuario'
        }),
        label='Usuário',
        max_length=30,
        min_length=6,
        required=True,
        error_messages={
            'required': 'Preencha este campo.',
            'min_length': 'Usuário deve ter no mínimo 6 caracteres.'
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '********'
        }),
        label='Senha',
        max_length=30,
        min_length=8,
        required=True,
        error_messages={
            'required': 'Preencha este campo.',
            'min_length': 'A senha deve ter no mínimo 8 caracteres.',
        }
    )

    def clean_username(self):
        username = (self.cleaned_data.get('username') or '').strip()

        if not re.fullmatch(r"[A-Za-z0-9]+", username):
            raise ValidationError("Deve conter apenas letras e números.") 

        return username
    

class CadastroForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'exemplousuario'
        }),
        label='Usuário',
        max_length=30,
        min_length=6,
        required=True,
        error_messages={
            'required': 'Usuário deve ter no mínimo 6 caracteres.',
            'min_length': 'Usuário deve ter no mínimo 6 caracteres.'
        }
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'seu@email.com'
        }),
        label='Email',
        max_length=100,
        required=True,
        error_messages={
            'required': 'E-mail é obrigatório.',
            'invalid': 'E-mail inválido.'
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '********'
        }),
        label='Senha',
        max_length=30,
        min_length=8,
        required=True,
        error_messages={
            'required': 'A senha deve ter no mínimo 8 caracteres.',
            'min_length': 'A senha deve ter no mínimo 8 caracteres.'
        }
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '********'
        }),
        label='Senha',
        max_length=30,
        min_length=8,
        required=True,
        error_messages={
            'required': 'A senha deve ser igual.',
            'min_length': 'A senha deve ter no mínimo 8 caracteres.'
        }
    )


    def clean_username(self):
        username = (self.cleaned_data.get('username') or '').strip()

        if not re.fullmatch(r"[A-Za-z0-9]+", username):
            raise ValidationError("Deve conter apenas letras e números.") 

        if User.objects.filter(username=username).exists():
            raise ValidationError("Este usuário já está cadastrado.")

        return username
    
    def clean_email(self):
        email = (self.cleaned_data.get('email') or '').strip().lower()
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este email já está cadastrado.')
        
        return email

    def clean_password(self):
        password = (self.cleaned_data.get('password') or '')

        if password.isdigit():
            raise ValidationError("A senha não pode conter apenas números.")

        return password 
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password") 
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("As senhas não coicidem.")

        return cleaned_data
     

class RecuperarForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'seu@email.com'
        }),
        label='Email',
        max_length=100,
        required=True,
        error_messages= {
            'required': 'E-mail é obrigatório.',
            'invalid': 'E-mail inválido.'
        }
    )

    
    def clean_email(self):
        email = (self.cleaned_data.get('email') or '').strip().lower()
            
        return email