from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from core.forms import LoginForm
from .services import client_services , vehicles_services, servicos_services
from core.services.client_services import get_db
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse ## Vamos utilizar para criar os charts, acho que talvez com Charts.Js
import core.services.utils as utils
# Create your views here.

""" def index(request):
    return render(request, 'index.html') """

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
        return redirect("login")
    return render(request,"logout.html")
    

@login_required
def dashboard(request):
    kpi_data = utils.kpis()
    
    return render(request, 'dashboard.html', context={
        'kpi_data': kpi_data,
        'user': request.user.username
    })


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

            return redirect(f"{reverse('vizualizar_cliente')}?documento={data['documento']}")
        
        except Exception as e:
            return render(request, 'cadastro_cliente.html', {
                'success': False,
                'error': str(e),
                'data': data
            })
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

    client = client_services.get_client(documento)
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

    vehicles = vehicles_services.list_vehicles_by_documento(documento)
    servicos_abertos = servicos_services.get_open_services_by_client_document(documento)
    servicos_finalizados = servicos_services.get_completed_services_by_client_document(documento)
    return render(request, 'vizualizar_cliente.html', {
        'client': client,
        'vehicles': vehicles,
        'services': servicos_services.count_services_by_client_document(documento),
        'servicos_abertos': servicos_abertos,
        'servicos_finalizados': servicos_finalizados,
    })


@login_required
def cadastro_veiculo(request):
    documento_cliente = request.GET.get('documento')

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
        return render(request, 'cadastro_veiculo.html', {'documento_cliente': documento_cliente})


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

@login_required
def listar_servicos(request):
    if request.method == 'GET':
        services = servicos_services.show_services()
        return render(request, 'listar_servicos.html', context={'services': services})
    if request.method == 'POST':
        service_id = request.POST.get('codigo')
        servicos_services.delete_service(service_id)
        return redirect('listar_servicos')
    return render(request, 'listar_servicos.html')

@login_required
def cadastro_servico(request):
    
    if request.method == 'GET':
        documento_cliente = request.GET.get('documento')
        if not documento_cliente:
            return redirect('listar_clientes')
        placa = request.GET.get('placa')
        if not placa:
            return redirect('listar_veiculos')
        return render(request, 'cadastro_servico.html', {
            'documento_cliente': documento_cliente,
            'placa_veiculo': placa
        })
    if request.method == 'POST':
        documento_cliente = request.GET.get('documento')
        placa = request.GET.get('placa')
        if not documento_cliente or not placa:
            return redirect('listar_clientes')
        data = {
            "tipo": request.POST.get('tipo'),
            "descricao": request.POST.get('descricao'),
            "preco": alterar_br_para_float(request.POST.get('valor_unitario', 0.0)),
            "prazo_execucao": datetime.fromisoformat(request.POST.get('prazo_execucao', datetime.now().isoformat())),
            "data_inicio": datetime.fromisoformat(request.POST.get('data_inicio', datetime.now().isoformat())),
            "quantidadeRodas": int(request.POST.get('quantidade_rodas', 1)),
            "duracao": request.POST.get('tempo_execucao', 0),
            "status": request.POST.get('status', 'ativo'),
            "documento_cliente": documento_cliente,
            "placa_veiculo": placa,  
        }
        try:
            servicos_services.register_service(data)
            return redirect('listar_servicos')
        except Exception as e:
            print(f"Erro ao cadastrar serviço: {e}")
            return render(request, 'cadastro_servico.html', {'error': str(e), 'data': data})

    return render(request, 'cadastro_servico.html')

@login_required
def editar_servico(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')
        if not codigo:
            return redirect('listar_servicos')

        service = servicos_services.get_service(codigo)
        if not service:
            return redirect('listar_servicos')
        return render(request, 'editar_servico.html', {'service': service})

    if request.method == 'POST':
        codigo = request.GET.get('codigo')
        new_data= {
            "tipo": request.POST.get("tipo"),
            "descricao": request.POST.get("descricao"),
            "preco": alterar_br_para_float(request.POST.get("preco", 0.0)),
            "prazo_execucao": datetime.fromisoformat(request.POST.get('prazo_execucao', datetime.now().isoformat())),
            "data_inicio": datetime.fromisoformat(request.POST.get('data_inicio', datetime.now().isoformat())),
            "quantidadeRodas": int(request.POST.get("quantidade_rodas", 1)),
            "duracao": request.POST.get("duracao", 0),
            "status": request.POST.get("status", "ativo"),
        }
        success = servicos_services.update_service(codigo, new_data)
        if success:
            return redirect('listar_servicos')
        else:
            error = "Erro ao atualizar serviço."
            return render(request, 'editar_servico.html', {'service': new_data, 'error': error})

    return render(request, 'editar_servico.html', {'service': service})

@login_required
def finalizar_servico(request):
    codigo = request.GET.get('codigo')
    if not codigo:
        return redirect('listar_servicos')

    service = servicos_services.get_service(codigo)
    if not service:
        return redirect('listar_servicos')

    if request.method == 'POST':
        try:
            servicos_services.finish_service(codigo)
            return redirect('listar_servicos')
        except Exception as e:
            error = str(e)
            return render(request, 'finalizar_servico.html', {'service': service, 'error': error})

    return render(request, 'finalizar_servico.html', {'service': service})

@login_required
def cancelar_servico(request, codigo):
    if request.method == 'GET':
        if not codigo:
            print("Código do serviço não fornecido.")
            return redirect('listar_servicos')

        service = servicos_services.get_service(codigo)
        if not service:
            print("Serviço não encontrado.")
            return redirect('listar_servicos')
        
        if service.get('status', '').lower() != 'ativo':
            print("Serviço não está ativo, não pode ser cancelado.")
            return redirect('listar_servicos')

        return render(request, 'cancelar_servico.html', {'servico': service})
        
    if request.method == 'POST':
        if not codigo:
            print("Código do serviço não fornecido.")
            return redirect('listar_servicos')

        servico = servicos_services.get_service(codigo)
        if not servico:
            print("Serviço não encontrado.")
            return redirect('listar_servicos')

        if request.method == 'POST':
            try:
                print("Tentando cancelar o serviço com código:", codigo)
                servicos_services.cancel_service(codigo)
                return redirect('listar_servicos')
            except Exception as e:
                error = str(e)
                return render(request, 'cancelar_servico.html', {'servico': service, 'error': error})
        return render(request, 'cancelar_servico.html', {'servico': service})

@login_required
def excluir_servico(request):
    codigo = request.GET.get('codigo')
    if not codigo:
        return redirect('listar_servicos')

    service = servicos_services.get_service(codigo)
    if not service:
        return redirect('listar_servicos')

    if request.method == 'POST':
        deleted = servicos_services.delete_service(codigo)
        if deleted:
            return redirect('listar_servicos')
        else:
            error = "Falha ao excluir serviço."
            return render(request, 'excluir_servico.html', {'service': service, 'error': error})

    return render(request, 'excluir_servico.html', {'service': service})

@login_required
def vizualizar_servico(request):
    codigo = request.GET.get('codigo')
    servico = servicos_services.get_service(codigo)
    if not servico:
        return redirect('listar_servicos')
    status = servico.get('status', '').lower()
    data_cancelamento = None
    if status == 'cancelado':
        data_cancelamento = servico.get('data_fechamento')
    return render(request, 'vizualizar_servico.html', {
        'servico': servico,
        'status': status,
        'data_cancelamento': data_cancelamento,
    })

@login_required
def servicos_finalizados(request):
    finalizados = []
    finalizados = servicos_services.show_completed_services()
    return render(request, 'servicos_finalizados.html', {'services': finalizados})

@login_required
def visualizar_servicos_cancelados(request):
    cancelados = servicos_services.show_canceled_services()
    return render(request, 'servicos_cancelados.html', {'services': cancelados})

def alterar_br_para_float(value):
    if isinstance(value, float):
        return value
    if isinstance(value, int):
        return float(value)
    if isinstance(value, str):
        value = value.replace('.', '').replace(',', '.')
        try:
            return float(value)
        except Exception:
            return 0.0
    return 0.0