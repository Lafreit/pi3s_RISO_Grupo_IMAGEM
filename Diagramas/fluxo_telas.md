graph TD
    %% Telas principais
    Login("Tela de Login")
    Gerencia("Tela de Gerência")
    Clientes("Tela de Clientes")
    CadastroClientes("Tela de Cadastro de Clientes")
    AtualizarCadastro("Tela de Atualizar Cadastro")
    ListaClientes("Tela de Lista de Clientes")
    CadastroVeiculos("Tela de Cadastro de Veículos")
    OrdemServico("Tela de Ordem de Serviço")
    VisualizarOS("Tela de Visualizar OS")
    Departamento("Tela de Departamento")
    Empregados("Tela de Empregados")

    %% Mensagens
    LoginNaoCadastrado("Mensagem: Usuário não cadastrado. Solicite seu cadastro ao Gerente.")
    SenhaInvalida("Mensagem: Senha inválida. Tente novamente.")
    CadastroSucesso("Mensagem: Cadastro realizado com sucesso!")
    VeiculoCadastradoSucesso("Mensagem: Veículo cadastrado com sucesso!")
    OrdemServicoConcluida("Ordem de Serviço (Data Conclusão preenchida)")
    OrdemServicoImprimir("Ordem de Serviço (Gera .pdf)")
    AtualizarCadastroPreenchido("Atualizar Cadastro (dados preenchidos)")


    %% Fluxo de Login
    Login -- Usuário cadastrado e senha válida --> PermissaoCheck{Checar Permissões}
    Login -- Usuário não cadastrado --> LoginNaoCadastrado
    Login -- Senha inválida --> SenhaInvalida

    PermissaoCheck -- Superusuário --> Gerencia
    PermissaoCheck -- Vendedor --> Clientes
    PermissaoCheck -- Montador --> OrdemServico
    PermissaoCheck -- Mecânico --> OrdemServico

    %% Fluxo da Tela de Gerência
    Gerencia -- Botão DEPARTAMENTO --> Departamento
    Gerencia -- Botão EMPREGADOS --> Empregados
    Gerencia -- Botão CLIENTES --> Clientes
    Gerencia -- Botão ORDEM DE SERVIÇO --> OrdemServico

    %% Fluxo da Tela de Clientes (Vendedor)
    Clientes -- Botão CADASTRO DE CLIENTE --> CadastroClientes
    Clientes -- Botão LISTA DE CLIENTES --> ListaClientes
    Clientes -- Botão VEÍCULOS --> CadastroVeiculos
    Clientes -- Botão LOGOFF --> Login

    %% Fluxo da Tela de Cadastro de Clientes
    CadastroClientes -- Botão Cadastrar Cliente --> ConfirmacaoCadastro{Validar Campos Obrigatórios}
    ConfirmacaoCadastro -- Campos OK --> CadastroSucesso
    CadastroClientes -- Botão Atualizar Cadastro --> AtualizarCadastro
    CadastroClientes -- Botão Cadastrar Veículo --> CadastroVeiculos
    CadastroClientes -- Botão CLIENTES --> Clientes

    %% Fluxo da Tela de Atualizar Cadastro
    AtualizarCadastro -- Preenchimento CNPJ/CPF --> AtualizarCadastroPreenchido
    AtualizarCadastro -- Botão Cadastro Atualizado --> CadastroVeiculos

    %% Fluxo da Tela de Lista de Clientes
    ListaClientes -- Botão CLIENTES --> Clientes
    ListaClientes -- Botão LOGOFF --> Login

    %% Fluxo da Tela de Cadastro de Veículos
    CadastroVeiculos -- Botão VEICULO CADASTRADO --> VeiculoCadastradoSucesso
    CadastroVeiculos -- Botão ORDEM DE SERVIÇO --> OrdemServico

    %% Fluxo da Tela de Ordem de Serviço
    OrdemServico -- Seleção Concluído (Status da OS) --> OrdemServicoConcluida
    OrdemServico -- Botão Visualizar OS --> VisualizarOS
    OrdemServico -- Botão Imprimir --> OrdemServicoImprimir

    %% Observações adicionais sobre os campos e funcionalidades
    subgraph Detalhes da Tela de Login
        Login -- Campo Nome do Usuário --> Login
        Login -- Campo Senha --> Login
    end

    subgraph Detalhes da Tela de Cadastro de Clientes
        CadastroClientes -- Campo Nome Completo ou Razão Social (obrigatório) --> CadastroClientes
        CadastroClientes -- Checkbox CNPJ --> CadastroClientes
        CadastroClientes -- Campos: CPF/CNPJ, CEP, Rua, Número (obrigatório), Complemento, Bairro, Cidade, Estado --> CadastroClientes
    end

    subgraph Detalhes da Tela de Atualizar Cadastro
        AtualizarCadastro -- Checkbox CNPJ --> AtualizarCadastro
        AtualizarCadastro -- Campo CNPJ ou CPF --> AtualizarCadastro
    end

    subgraph Detalhes da Tela de Lista de Clientes
        ListaClientes -- Lista: ID, NOME COMPLETO, EMAIL, TELEFONE, CPF/CNPJ --> ListaClientes
    end

    subgraph Detalhes da Tela de Cadastro de Veículos
        CadastroVeiculos -- Checkbox Motocicleta --> CadastroVeiculos
        CadastroVeiculos -- Checkbox Automóvel --> CadastroVeiculos
        CadastroVeiculos -- Campos: Placa (obrigatório), Quilometragem (obrigatório), Marca (obrigatório), Modelo (obrigatório), Ano (obrigatório), Cor --> CadastroVeiculos
    end

    subgraph Detalhes da Tela de Ordem de Serviço
        OrdemServico -- Campo Código da OS (auto gerado) --> OrdemServico
        OrdemServico -- Campo Cliente (último cadastrado) --> OrdemServico
        OrdemServico -- Campo CPF/CNPJ (último cliente) --> OrdemServico
        OrdemServico -- Dados do Veículo: Placa, Modelo, Ano, Cor (último veículo) --> OrdemServico
        OrdemServico -- Dropdown Mecânico/Montador --> OrdemServico
        OrdemServico -- Campo Data de Abertura (auto preenchido) --> OrdemServico
        OrdemServico -- Campo Hora da Abertura (auto preenchido) --> OrdemServico
        OrdemServico -- Campo Data da Conclusão (ao concluir OS) --> OrdemServico
        OrdemServico -- Tabela Serviços/Produtos --> OrdemServico
        OrdemServico -- Dropdown Cod. Item (Cadastro de Serviços) --> OrdemServico
        OrdemServico -- Text Area Observações/Anotações --> OrdemServico
        OrdemServico -- Dropdown Status da OS --> OrdemServico
    end