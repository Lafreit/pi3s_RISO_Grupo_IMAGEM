from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from core.forms import LoginForm
from .services import user_services, client_services , vehicles_services
from core.services.client_services import get_db
from django.urls import reverse

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

from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def cadastro_cliente(request):
    if request.method == 'POST':
        data = {
            "nome": request.POST.get('nome'),
            "documento": request.POST.get('documento'),
            "cep": request.POST.get('cep'),
            "email": request.POST.get('email'),
            "telefone": request.POST.get('telefone'),
            "telefone_residencial": request.POST.get('telefone_residencial'),
        }
        try:
            client_services.create_client(data)
            return render(request, 'cadastro_cliente.html', {'success': True, 'data': data})
        except Exception as e:
            return render(request, 'cadastro_cliente.html', {'success': False, 'error': str(e), 'data': data})
    else:
        return render(request, 'cadastro_cliente.html', {'success': False})


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

    # Buscar veículos vinculados a esse cliente
    vehicles = vehicles_services.list_vehicles_by_documento(documento)  # método que vamos criar

    return render(request, 'vizualizar_cliente.html', {
        'client': client,
        'vehicles': vehicles,
    })


@login_required
def cadastro_veiculo(request):
    documento_cliente = request.GET.get('documento')  # pega o documento do cliente na URL

    if request.method == 'POST':
        data = {
            "tipo": request.POST.get('tipo'),
            "placa": request.POST.get('placa'),
            "marca": request.POST.get('marca'),
            "modelo": request.POST.get('modelo'),
            "ano": request.POST.get('ano'),
            "quilometragem": request.POST.get('quilometragem'),
            "cor": request.POST.get('cor'),
            "observacoes": request.POST.get('observacoes'),
            "documento_cliente": request.POST.get('documento_cliente'),  # pega do form POST
        }
        try:
            vehicles_services.register_vehicle(data)
            return redirect('listar_veiculos')
        except Exception as e:
            return render(request, 'cadastro_veiculo.html', {'error': str(e), 'data': data})

    else:
        # Quando for GET, já envia o documento do cliente para o formulário
        return render(request, 'cadastro_veiculo.html', {'documento_cliente': documento_cliente})


from django.urls import reverse

@login_required
def editar_veiculo(request):
    placa = request.GET.get('placa') or request.POST.get('placa')
    if not placa:
        return redirect('listar_veiculos')

    vehicle = vehicles_services.get_vehicle(placa)
    if not vehicle:
        return redirect('listar_veiculos')

    if request.method == 'POST':
        new_data = {
            "tipo": request.POST.get("tipo"),
            "marca": request.POST.get("marca"),
            "modelo": request.POST.get("modelo"),
            "ano": request.POST.get("ano"),
            "quilometragem": request.POST.get("quilometragem"),
            "cor": request.POST.get("cor"),
            "observacoes": request.POST.get("observacoes"),
        }
        success = vehicles_services.update_vehicle(placa, new_data)
        if success:
            url = f"{reverse('vizualizar_cliente')}?documento={vehicle.get('documento_cliente')}"
            return redirect(url)
        else:
            error = "Erro ao atualizar veículo."
            return render(request, 'editar_veiculo.html', {'vehicle': new_data, 'error': error})

    return render(request, 'editar_veiculo.html', {'vehicle': vehicle})

@login_required
def listar_veiculos(request):
    vehicles = vehicles_services.list_vehicles()
    return render(request, 'listar_veiculos.html', {'vehicles': vehicles})

@login_required
def editar_veiculo(request):
    placa = request.GET.get('placa') or request.POST.get('placa')
    if not placa:
        return redirect('listar_veiculos')

    vehicle = vehicles_services.get_vehicle(placa)
    if not vehicle:
        return redirect('listar_veiculos')

    if request.method == 'POST':
        data = {
            "tipo": request.POST.get("tipo"),
            "marca": request.POST.get("marca"),
            "modelo": request.POST.get("modelo"),
            "ano": request.POST.get("ano"),
            "quilometragem": int(request.POST.get("quilometragem", 0)),
            "cor": request.POST.get("cor"),
            "observacoes": request.POST.get("observacoes"),
        }
        try:
            updated = vehicles_services.update_vehicle(placa, data)
            if updated:
                return redirect('listar_veiculos')
            else:
                error = "Falha ao atualizar veículo."
        except Exception as e:
            error = str(e)

        return render(request, 'editar_veiculo.html', {'vehicle': data, 'error': error})
    
    return render(request, 'editar_veiculo.html', {'vehicle': vehicle})

@login_required
def excluir_veiculo(request):
    placa = request.GET.get('placa') or request.POST.get('placa')
    if not placa:
        return redirect('listar_veiculos')

    vehicle = vehicles_services.get_vehicle(placa)
    if not vehicle:
        return redirect('listar_veiculos')

    if request.method == 'POST':
        deleted = vehicles_services.delete_vehicle(placa)
        if deleted:
            return redirect('listar_veiculos')
        else:
            error = "Falha ao excluir veículo."
            return render(request, 'excluir_veiculo.html', {'vehicle': vehicle, 'error': error})

    return render(request, 'excluir_veiculo.html', {'vehicle': vehicle})

@login_required
def vizualizar_veiculo(request):
    placa = request.GET.get('placa')
    if not placa:
        return redirect('listar_veiculos')

    vehicle = vehicles_services.get_vehicle(placa)
    if not vehicle:
        return redirect('listar_veiculos')

    documento_cliente = vehicle.get('documento_cliente')
    cliente = None
    if documento_cliente:
        cliente = client_services.get_client(documento_cliente)

    return render(request, 'vizualizar_veiculo.html', {
        'vehicle': vehicle,
        'cliente': cliente
    })
