from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def dashboard(request):
    return render(request, 'workspace/dashboard.html')

@login_required
def tarefas(request):
    return render(request, 'workspace/tarefas.html')

@login_required
def contatos(request):
    return render(request, 'workspace/contatos.html')

@login_required
def conversas(request):
    return render(request, 'workspace/conversas.html')

@login_required
def agenda(request):
    return render(request, 'workspace/agenda.html')

def logout_view(request):
    logout(request)
    return redirect('login')
