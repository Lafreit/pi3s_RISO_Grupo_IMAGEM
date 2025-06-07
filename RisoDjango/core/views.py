from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from core.forms import LoginForm
from .services import user_services, client_services 
from core.services.client_services import get_db

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.user.id is not None:
        return redirect("dashboard")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("dashboard")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("index")
    return render(request,"logout.html")
    

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def cadastro_cliente(request):
    if request.method == 'POST':
        try:
            data = {
                "nome": request.POST.get('nome'),
                "documento": request.POST.get('documento'),
                "cep": request.POST.get('cep'),
                "email": request.POST.get('email'),
                "telefone": request.POST.get('telefone'),
                "telefone_residencial": request.POST.get('telefone_residencial'),
            }
            client_services.create_client(data)
            return redirect('listar_clientes')
        except Exception as e:
            print(f"Error creating client: {e}")
            return render(request, 'cadastro_cliente.html', context={'success': False, 'error': str(e), 'data': data})
    if request.method == 'GET':
        return render(request, 'cadastro_cliente.html', context={'success': False})

@login_required
def listar_clientes(request):
    if request.method == 'GET':
        clients = client_services.list_clients()
        return render(request, 'listar_clientes.html', context={'clients': clients})
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client_services.delete_client(client_id)
        return redirect('listar_clientes')
    return render(request, 'listar_clientes.html')

@login_required
def editar_cliente(request):
    documento = request.GET.get('documento') or request.POST.get('documento')
    if not documento:
        return redirect('listar_clientes')

    client = client_services.get_client(documento)
    if not client:
        return redirect('listar_clientes')

    if request.method == 'POST':
        data = {
            "nome": request.POST.get("nome"),
            "documento": request.POST.get("documento"),
            "cep": request.POST.get("cep"),
            "email": request.POST.get("email"),
            "telefone": request.POST.get("telefone"),
            "telefone_residencial": request.POST.get("telefone_residencial"),
        }

        try:
            client_services.update_client(documento, data)
            return redirect('listar_clientes')
        except ValueError as e:
            return render(request, 'editar_cliente.html', {
                'client': data,
                'error': str(e)
            })

    return render(request, 'editar_cliente.html', {'client': client})

@login_required
def excluir_cliente(request):
    documento = request.GET.get('documento') or request.POST.get('documento')
    if not documento:
        return redirect('listar_clientes')

    client = get_db()["clients"].find_one({"documento": documento})
    if not client:
        return redirect('listar_clientes')

    if request.method == 'POST':
            deleted = client_services.delete_client(documento)
            if deleted:
                return redirect('listar_clientes')

@login_required
def vizualizar_cliente(request):
    documento = request.GET.get('documento')
    if not documento:
        return redirect('listar_clientes')

    client = client_services.get_client(documento)
    if not client:
        return redirect('listar_clientes')

    return render(request, 'vizualizar_cliente.html', {'client': client})
