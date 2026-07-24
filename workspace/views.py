from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ContactForm
from .models import Contact

@login_required
def dashboard(request):
    return render(request, 'workspace/dashboard.html')

@login_required
def tarefas(request):
    return render(request, 'workspace/tarefas.html')

@login_required
def contatos(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('contatos')

    else:
        form = ContactForm()

    contact = Contact.objects.all()

    return render(request, 'workspace/contatos.html', {
        'form': form,
        'contacts': contact
    })

@login_required
def conversas(request):
    return render(request, 'workspace/conversas.html')

@login_required
def agenda(request):
    return render(request, 'workspace/agenda.html')

def logout_view(request):
    logout(request)
    return redirect('login')
