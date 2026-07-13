from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .forms import LoginForm, CadastroForm, RecuperarForm
from django.views.decorators.cache import never_cache
from django.contrib import messages

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
            )

            return redirect('login')

    else:
        form = CadastroForm()

    return render(request, 'users/cadastro.html', {'form': form})

@never_cache
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            
            form.add_error(None, "Usuário ou senha inválidos. Verifique seus dados de login e tente novamente.")
    else: 
        form = LoginForm()

    return render(request, "users/login.html", {'form': form})

def forgot_view(request):
    if request.method == "POST":
        form = RecuperarForm(request.POST) 

        if form.is_valid():
            email = form.cleaned_data['email']

            email_exists = User.objects.filter(email=email).exists()

            if email_exists:
                return redirect('login')
            else:
                form.add_error(None, "Este e-mail não está cadastrado.")

    else:
        form = RecuperarForm()

    return render(request, "users/forgot_password.html", {'form': form})