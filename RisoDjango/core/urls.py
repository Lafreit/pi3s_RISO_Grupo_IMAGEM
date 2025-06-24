from django.urls import path
from core.views import cadastro_cliente, login, logout, listar_clientes, dashboard, listar_clientes, excluir_cliente, editar_cliente, vizualizar_cliente, cadastro_veiculo, editar_veiculo, listar_veiculos, excluir_veiculo, vizualizar_veiculo, listar_servicos, editar_servico,  vizualizar_servico, visualizar_servicos_cancelados ,cadastro_servico, excluir_servico,cancelar_servico, finalizar_servico, servicos_finalizados



urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro-cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('listar-clientes/', listar_clientes, name='listar_clientes'),
    path('editar_cliente/', editar_cliente, name='editar_cliente'),
    path('clientes/excluir/', excluir_cliente, name='excluir_cliente'),
    path('vizualizar_cliente/', vizualizar_cliente, name='vizualizar_cliente'),
    path("cadastro_veiculo/", cadastro_veiculo, name="cadastro_veiculo"),
    path('veiculos/', listar_veiculos, name='listar_veiculos'),
    path('editar_veiculo/', editar_veiculo, name='editar_veiculo'),
    path('excluir_veiculo/', excluir_veiculo, name='excluir_veiculo'),
    path('vizualizar_veiculo/', vizualizar_veiculo, name='vizualizar_veiculo'),
    path('cadastro-servico/', cadastro_servico, name='cadastro_servico'),
    path('listar-servicos/', listar_servicos, name='listar_servicos'),
    path('editar-servicos/', editar_servico, name='editar_servico'),
    path('excluir_servico/', excluir_servico, name='excluir_servico'),
    path('cancelar_servico/<str:codigo>/', cancelar_servico, name='cancelar_servico'),
    path('vizualizar_servico/', vizualizar_servico, name='vizualizar_servico'),
    path('servicos_cancelados/', visualizar_servicos_cancelados, name='servicos_cancelados'),
    path('finalizar_servico/', finalizar_servico, name='finalizar_servico'),
    path('servicos-finalizados/', servicos_finalizados, name='servicos_finalizados'),
    # path('cadastro-usuario/', cadastro_cliente, name='cadastro_usuario'),
    # path('listar-usuarios/', listar_clientes, name='listar_usuarios'),
    # path('editar-usuarios/<int:user_id>/', editar_cliente, name='editar_usuarios'),
    # path('deletar-usuarios/<int:user_id>/', editar_cliente, name='deletar_usuarios'),
]
