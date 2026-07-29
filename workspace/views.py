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
    total_contacts = Contact.objects.count()
    replied_contacts = Contact.objects.filter(status='respondido').count()
    new_contacts = Contact.objects.filter(status='novo').count()
    pending_contacts = Contact.objects.filter(status='pendente').count()

        
    context = {
        'form': form,
        'contacts': contact,
        'total_contacts' : total_contacts,
        'replied_contacts' : replied_contacts,
        'new_contacts' : new_contacts, 
        'pending_contacts' : pending_contacts,
    }

    return render(request, 'workspace/contatos.html', context)

@login_required
def conversas(request):
    return render(request, 'workspace/conversas.html')

@login_required
def agenda(request):
    return render(request, 'workspace/agenda.html')

def logout_view(request):
    logout(request)
    return redirect('login')
