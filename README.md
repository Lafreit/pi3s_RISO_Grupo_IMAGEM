# pi3s_RISO_Grupo_IMAGEM

Este repositório destina-se ao desenvolvimento do Projeto RISO, pelo Grupo IMAGEM, relativo ao PI do 3º semestre do curso de DSM da FATEC/CPS/Araras.

# Grupo IMAGEM

Os alunos desenvolvedores que integram o grupo IMAGEM, responsáveis pelo desenvolvimento do Projeto RISO, no contexto do Projeto Interdisciplinar do 3º semestre do curso de Desenvolvimento de Software Multiplataforma da Fatec de Araras, que integra o Centro Paula Souza do Estado de São Paulo, são:
  
  Casemiro Seneme - casemiro.seneme@fatec.sp.gov.br
  
  Eduardo William Zarnelli Júnior - dduzarnelli@gmail.com
  
  Izabely do Nascimento Rodrigues de Campos - iza.rodrigues@gmail.com
  
  João Vitor de Camargo - joavitordecamargo7@gmail.com
  
  Luíz Antônio de Freitas - lafreitas2@yahoo.com.br

  Rafael Botezelli - rafaelbotezelli@gmail.com 

  Vitor Eduardo de Barros Marciano
  vitor.marciano001@gmail.com

# Product Backlog

O projeto visa desenvolver um software para um cliente que tem como atividade a prestação de serviços de recuperação de rodas, como soldagem, desempeno, diamantação, outros serviços relacionados à suspensão e sistema de freio, e a venda de pneus e peças. Para isso, este cliente necessita de um software para a gestão seu negócio, para cadastrar clientes, veículos, como carros e motos, serviços de soldagem e desempeno de rodas, cadastrar os produtos, controlar estoque, cadastrar as vendas, emitir ordem de serviço para a oficina e para o salão de serviços, um controle básico do fluxo de caixa diário, cadastrar os empregados, mecânicos, vendedores e gerente, e para cada uma dessas atividades, emitir relatórios.
Os módulos deste software devem ser integrados, possuir um dashboard com as informações integradas e dashboards para cada módulo.
O cliente no áudio enviado estabelece algumas necessidades prioritárias que são: cadastro de clientes (endereço, CPF/CNPJ, etc.), cadastro de veículos (placa, marca, modelo, ano, quilometragem, etc.), cadastro de produtos (vendas de pneu, marca, venda de serviços, quantidade, valor, etc.) e forma de pagamento (à vista, dinheiro, PIX, cartão de crédito).
Diante da necessidade apresentada pelo cliente, faz-se necessário repensar o projeto apresentado para ajustá-lo às necessidades dele.

# VISÃO GERAL:

Módulo 1: Módulo de Login
Módulo 2: Cadastro de Clientes
Módulo 3: Cadastro de Veículos
Módulo 4: Cadastro de Serviços
Módulo 5: Estoque
Módulo 6: Cadastrar Vendas
Módulo 7: Cadastrar Ordem de Serviço
Módulo 8: Cadastrar Fluxo de Caixa
Módulo 9: Cadastro de Departamentos
Módulo 10: Cadastro de Empregados

# FLUXOGRAMA DO PROJETO:

Este é o diagrama do nosso Product Backlog:

![Diagrama do Product Backlog](Diagramas/fluxograma.svg)

# Product Backlog Projeto RISO (Descritivo)

Os critérios definidos para o Product Backlog do Projeto RISO as recomendações técnicas para se definir a História do Usuário (User Story) quanto a propósito, formato e características, assim definidos:
Propósito: Descrever uma funcionalidade do sistema do ponto de vista do usuário final ou de um stakeholder. Ela foca no valor que essa funcionalidade entrega e em quem a utilizará.
Formato Comum: Geralmente segue o formato: "Como um [tipo de usuário], eu quero [algum objetivo] para que [algum motivo/benefício]".
Características:
Curta e concisa: Deve ser breve o suficiente para caber em um cartão ou post-it.
Centrada no usuário: Coloca o usuário no centro da necessidade.
Estimável: Deve ser possível para a equipe de desenvolvimento estimar o esforço necessário para implementá-la.
Negociável: Os detalhes podem ser discutidos e ajustados entre o time de desenvolvimento e o Product Owner.
Valiosa: Entrega valor para o usuário ou para o negócio.
Testável: Deve ser possível definir critérios para verificar se a história foi implementada corretamente.
Passamos à descrição de cada módulo do Projeto RISO.

# Módulo 1: Módulo de Login

User Story 1.1: Como um usuário, eu quero poder realizar login no sistema para acessar minhas funcionalidades e dados de forma segura… (detalhes dos Critérios de Aceitação).
User Story 1.2: Como um usuário, eu quero poder inserir meu nome de usuário e senha para me autenticar no sistema… (detalhes dos Critérios de Aceitação).
User Story 1.3: Como um usuário, eu quero ser notificado caso minhas credenciais estejam incorretas para poder tentar novamente… (detalhes dos Critérios de Aceitação).
User Story 1.4: Como um usuário, eu quero ter a opção de "lembrar meu usuário" para facilitar logins futuros (se aplicável)… (detalhes dos Critérios de Aceitação).
User Story 1.5: Como um usuário, eu quero ter a opção de "esqueci minha senha" para poder recuperá-la caso necessário… (detalhes dos Critérios de Aceitação).
User Story 1.6: Como um administrador, eu quero poder gerenciar os usuários do sistema (criar, editar, desativar)… (detalhes dos Critérios de Aceitação).
User Story 1.7: Como um administrador, eu quero poder definir os níveis de acesso para diferentes tipos de usuários… (detalhes dos Critérios de Aceitação).

# Módulo 2: Cadastro de Clientes

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo cliente informando seu nome completo ou razão social... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o endereço do cliente (CEP, rua, número, complemento, bairro, cidade, estado)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o CPF para clientes pessoa física e o CNPJ para clientes pessoa jurídica... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar os meios de contato do cliente (telefone principal, telefone secundário opcional, e-mail opcional)... (detalhes dos Critérios de Aceitação)

# Módulo 3: Cadastro de Veículos

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo veículo informando o tipo (automóvel ou motocicleta)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a placa do veículo... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a marca e o modelo do veículo... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o ano de fabricação do veículo... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a quilometragem atual do veículo... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a cor do veículo (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de adicionar outras informações relevantes sobre o veículo (opcionalmente)... (detalhes dos Critérios de Aceitação)

# Módulo 4: Cadastro de Serviços

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo serviço informando um código de serviço único... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o tipo do serviço (ex: Balanceamento, Alinhamento, Reforma de Rodas)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar uma descrição detalhada do serviço (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o valor unitário do serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o tempo médio de execução do serviço (em horas ou minutos)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a quantidade padrão de rodas envolvidas no serviço (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar um prazo de entrega padrão para o serviço (opcionalmente, em dias)... (detalhes dos Critérios de Aceitação)

# Módulo 5: Estoque

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo produto informando um código único... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a marca do produto... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o tipo ou descrição do produto... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar outras especificações do produto (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de registrar a entrada de novos produtos no estoque, informando a data da entrada... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de selecionar o fornecedor do produto na entrada... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de informar a quantidade de produtos que estão entrando no estoque... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de registrar o valor unitário de compra do produto na entrada... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de registrar a saída de produtos do estoque, vinculando-a a um código de venda... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de registrar a data da saída do produto... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de informar a quantidade de produtos que estão saindo do estoque... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema calcule e exiba o saldo atual de cada produto... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de definir a capacidade máxima de estocagem para cada produto (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema me apresente alertas visuais sobre a capacidade de estocagem... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de definir uma quantidade mínima de estoque para cada produto... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero receber um alerta de compra quando a quantidade em estoque de um produto atingir ou ficar abaixo da quantidade mínima definida... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema calcule e exiba a média de venda diária de cada produto (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema forneça uma previsão de esgotamento do produto (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar relatórios dos produtos discriminados pelo ID... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do histórico de compras de produtos... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do histórico de vendas de produtos... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do saldo atual de todos os produtos... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório de alerta de compra de produtos... (detalhes dos Critérios de Aceitação)

# Módulo 6: Cadastrar Vendas

Como um usuário do sistema, eu quero ser capaz de criar um novo orçamento de serviços e/ou produtos... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de selecionar o empregado responsável pelo orçamento... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de definir um prazo de validade para o orçamento (em dias)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema calcule e exiba a data de validade do orçamento automaticamente... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao adicionar um item ao orçamento, eu quero ser capaz de especificar se é um produto ou um serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao adicionar um produto ao orçamento, eu quero ser capaz de selecionar o produto... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao adicionar um produto ao orçamento, eu quero que o sistema calcule o valor bruto total dos produtos e o valor do ICMS... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao adicionar um serviço ao orçamento, eu quero ser capaz de selecionar o serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao adicionar um serviço ao orçamento, eu quero que o sistema calcule o valor bruto total dos serviços e o valor do ISS... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema calcule o valor total a pagar do orçamento... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de converter um orçamento em uma venda... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema registre a data da venda automaticamente... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao converter um orçamento em venda, eu quero que o sistema mantenha o código do orçamento original... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema apresente os valores atualizados dos produtos e serviços na tela de venda... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema calcule o valor total da venda... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de emitir um relatório de orçamento... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao concluir uma venda, eu quero que o sistema emita automaticamente uma Ordem de Serviço (OS)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que a Ordem de Serviço gerada possa ser visualizada e impressa... (detalhes dos Critérios de Aceitação)

# Módulo 7: Cadastrar Ordem de Serviço

Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada Ordem de Serviço (OS)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de vincular um ou mais mecânicos responsáveis à Ordem de Serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema registre automaticamente a data e hora de entrada do veículo/serviço na Ordem de Serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de registrar a data e hora de saída (conclusão) do veículo/serviço na Ordem de Serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de vincular um cliente existente à Ordem de Serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de adicionar um ou mais produtos utilizados na Ordem de Serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de adicionar um ou mais serviços realizados na Ordem de Serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que a Ordem de Serviço possa ser gerada a partir de uma venda concluída... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de adicionar observações ou detalhes adicionais à Ordem de Serviço... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que a Ordem de Serviço possa ser visualizada e impressa... (detalhes dos Critérios de Aceitação)

# Módulo 8: Cadastrar Fluxo de Caixa

Como um usuário do sistema, ao registrar uma entrada ou saída, eu quero ser capaz de selecionar a forma de pagamento utilizada... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de inserir o valor da movimentação... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao registrar uma movimentação, eu quero poder vincular um cliente (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao registrar uma movimentação de entrada referente a uma venda, eu quero poder vincular essa movimentação ao código da venda correspondente (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao registrar uma movimentação de entrada referente a um serviço concluído, eu quero poder vincular essa movimentação ao código da Ordem de Serviço (OS) correspondente (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema registre automaticamente no fluxo de caixa as entradas referentes a vendas de produtos e recebimentos de serviços concluídos... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema registre automaticamente no fluxo de caixa as saídas referentes a compras de estoque e pagamentos de fornecedores... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de registrar manualmente outras entradas e saídas no fluxo de caixa, detalhando a descrição... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, se um pagamento for realizado com cartão de crédito parcelado, eu quero que o sistema agende automaticamente os recebimentos futuros no fluxo de caixa... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório de fechamento diário... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um extrato do fluxo de caixa por um período específico... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero visualizar um gráfico mostrando a porcentagem de cada forma de pagamento utilizada nas entradas... (detalhes dos Critérios de Aceitação)

# Módulo 9: Cadastro de Departamentos

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo departamento informando um código único para o departamento... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, ao cadastrar um departamento, eu quero ser capaz de vincular um ou mais empregados a este departamento, especificando o código do empregado e o seu cargo dentro deste departamento... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de visualizar os empregados alocados a cada departamento, juntamente com seus respectivos cargos dentro desse departamento... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório geral de todos os departamentos... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório específico para um departamento... (detalhes dos Critérios de Aceitação)

# Módulo 10: Cadastro de Empregados

Como um usuário do sistema, eu quero ser capaz de selecionar o departamento ao qual o empregado pertence... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada empregado... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar o código de dependentes do empregado (opcionalmente)... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de selecionar o cargo do empregado a partir de uma lista predefinida... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a nacionalidade do empregado... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a naturalidade do empregado... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a cidade e a Unidade Federativa (UF) de residência do empregado... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de cadastrar a data de nascimento do empregado... (detalhes dos Critérios de Aceitação)
Como um usuário do sistema, eu quero ser capaz de selecionar o estado civil do empregado a partir de uma lista... (detalhes dos Critérios de Aceitação)

# CRITÉRIOS DE ACEITAÇÃO (Acceptance Criteria):

Antes, uma digressão sobre o conceito de Critérios de Aceitação: é um conjunto de condições que um produto ou serviço deve cumprir para ser considerado pronto. Eles são uma ferramenta de comunicação entre equipes e partes interessadas.
Critérios de Aceitação (Acceptance Criteria):
Propósito: Definir as condições específicas que devem ser atendidas para que uma história de usuário seja considerada completa e funcionando corretamente. Eles servem como um guia para os desenvolvedores durante a implementação e como base para os testes.
Formato Comum: Geralmente são listados como itens (em bullet points ou numerados) que descrevem cenários específicos e o resultado esperado para cada um. Podem começar com frases como "Dado que...", "Quando...", "Então...".

# Características:

Específicos: Detalham o comportamento esperado do sistema em cenários particulares.
Mensuráveis: Devem ser formulados de forma que seja possível determinar objetivamente se foram atendidos ou não.
Alcançáveis: Devem ser realistas dentro do contexto do projeto.
Relevantes: Devem estar diretamente ligados à história de usuário.
Temporais (implícito): Geralmente se referem ao comportamento em um determinado momento ou após uma ação.
Testáveis: Fornecem a base para a criação de testes de aceitação.
Definição dos critérios de aceitação para cada módulo do Projeto RISO.

# CRITÉRIO DE ACEITAÇÃO MÓDULO  1: MÓDULO DE LOGIN

# Módulo 1: Módulo de Login

User Story 1.1: Como um usuário, eu quero poder realizar login no sistema para acessar minhas funcionalidades e dados de forma segura.


Critério de Aceitação 1.1.1: O sistema deve apresentar um formulário com campos para "Nome de Usuário" e "Senha".
Critério de Aceitação 1.1.2: O sistema deve validar as credenciais inseridas com as informações armazenadas no banco de dados de usuários autenticados.
Critério de Aceitação 1.1.3: Em caso de sucesso no login, o usuário deve ser redirecionado para a página principal do sistema, exibindo informações relevantes ao seu perfil (se aplicável).
Critério de Aceitação 1.1.4: O sistema deve registrar a data e hora do último login bem-sucedido do usuário.
User Story 1.2: Como um usuário, eu quero poder inserir meu nome de usuário e senha para me autenticar no sistema.


Critério de Aceitação 1.2.1: O campo "Nome de Usuário" deve aceitar caracteres alfanuméricos (a-z, A-Z, 0-9) e os seguintes símbolos: ponto (.), sublinhado (_), hífen (-).
Critério de Aceitação 1.2.2: O campo "Senha" deve mascarar os caracteres digitados com asteriscos (*) ou outro indicador de segurança.
Critério de Aceitação 1.2.3: O sistema deve permitir que o usuário copie e cole o nome de usuário e senha nos respectivos campos.
User Story 1.3: Como um usuário, eu quero ser notificado caso minhas credenciais estejam incorretas para poder tentar novamente.


Critério de Aceitação 1.3.1: Se o nome de usuário não for encontrado no sistema, uma mensagem clara e concisa como "Nome de usuário inválido" deve ser exibida.
Critério de Aceitação 1.3.2: Se a senha inserida não corresponder ao nome de usuário fornecido, uma mensagem clara e concisa como "Senha incorreta" deve ser exibida.
Critério de Aceitação 1.3.3: Após 5 tentativas consecutivas de login falhas, o sistema deve bloquear temporariamente a conta do usuário por 5 minutos, exibindo uma mensagem informativa sobre o bloqueio e o tempo restante.
User Story 1.4: Como um usuário, eu quero ter a opção de "lembrar meu usuário" para facilitar logins futuros (se aplicável).


Critério de Aceitação 1.4.1: O formulário de login deve conter um checkbox com a legenda "Lembrar meu usuário".
Critério de Aceitação 1.4.2: Se o checkbox estiver marcado e o login for bem-sucedido, o sistema deve armazenar o nome de usuário em um cookie seguro no navegador do usuário.
Critério de Aceitação 1.4.3: Ao retornar à página de login, se o cookie existir, o campo "Nome de Usuário" deve ser preenchido automaticamente.
User Story 1.5: Como um usuário, eu quero ter a opção de "esqueci minha senha" para poder recuperá-la caso necessário.


Critério de Aceitação 1.5.1: A página de login deve conter um link claramente visível com o texto "Esqueci minha senha?".
Critério de Aceitação 1.5.2: Ao clicar no link, o usuário deve ser redirecionado para uma página segura onde possa inserir seu nome de usuário ou endereço de e-mail associado à conta.
Critério de Aceitação 1.5.3: Após a submissão do nome de usuário ou e-mail, o sistema deve enviar um e-mail para o endereço cadastrado contendo um link único e temporário para redefinir a senha.
User Story 1.6: Como um administrador, eu quero poder gerenciar os usuários do sistema (criar, editar, desativar).


Critério de Aceitação 1.6.1: O sistema deve fornecer uma seção administrativa protegida por login de administrador, com uma lista de todos os usuários cadastrados, exibindo informações como nome de usuário, e-mail e status (ativo/inativo).
Critério de Aceitação 1.6.2: O administrador deve ter a funcionalidade de criar novos usuários, definindo um nome de usuário único, um endereço de e-mail válido e uma senha inicial (com a opção de forçar a troca no primeiro login).
Critério de Aceitação 1.6.3: O administrador deve poder editar as informações de um usuário existente, incluindo nome, e-mail e perfil de acesso. A edição da senha deve seguir um fluxo seguro (ex: solicitação da senha atual ou geração de um link de redefinição).
Critério de Aceitação 1.6.4: O administrador deve poder desativar um usuário, alterando seu status para inativo no sistema, impedindo o login, mas mantendo seus dados para referência futura. A reativação também deve ser possível.
User Story 1.7: Como um administrador, eu quero poder definir os níveis de acesso para diferentes tipos de usuários.


Critério de Aceitação 1.7.1: O sistema deve permitir a criação e gestão de diferentes perfis de acesso (ex: "Administrador", "Operador de Vendas", "Técnico"). Para cada perfil, o administrador deve poder definir permissões específicas para acessar diferentes módulos e funcionalidades do sistema.
Critério de Aceitação 1.7.2: Ao criar ou editar um usuário, o administrador deve poder associá-lo a um dos perfis de acesso definidos.
Critério de Aceitação 1.7.3: O sistema deve verificar o perfil de acesso do usuário logado antes de permitir o acesso a qualquer funcionalidade ou dado, garantindo que apenas usuários com as permissões adequadas possam interagir com eles.

# CRITÉRIO DE ACEITAÇÃO MÓDULO  2: CADASTRO DE CLIENTES

# Módulo 2: Cadastro de Clientes 

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo cliente informando seu nome completo ou razão social...


Critério de Aceitação 2.1.1: O sistema deve apresentar um campo obrigatório para "Nome Completo" (para pessoa física) ou "Razão Social" (para pessoa jurídica).
Critério de Aceitação 2.1.2: O sistema deve permitir o cadastro de clientes tanto como pessoa física quanto jurídica, com campos específicos para cada tipo.
Critério de Aceitação 2.1.3: O sistema deve validar se o "Nome Completo" ou "Razão Social" possui um mínimo de caracteres (a definir).
Critério de Aceitação 2.1.4: Ao salvar o cliente, o sistema deve gerar um ID único para identificação.
Como um usuário do sistema, eu quero ser capaz de cadastrar o endereço do cliente (CEP, rua, número, complemento, bairro, cidade, estado)...


Critério de Aceitação 2.2.1: O sistema deve apresentar campos para "CEP", "Rua", "Número" (obrigatório), "Complemento" (opcional), "Bairro", "Cidade" e "Estado" (com uma lista de seleção das Unidades Federativas do Brasil).
Critério de Aceitação 2.2.2: O sistema deve integrar com um serviço de busca de CEP (se disponível) para preencher automaticamente os campos de rua, bairro, cidade e estado ao inserir um CEP válido.
Critério de Aceitação 2.2.3: O sistema deve validar o formato do CEP inserido.
Como um usuário do sistema, eu quero ser capaz de cadastrar o CPF para clientes pessoa física e o CNPJ para clientes pessoa jurídica...


Critério de Aceitação 2.3.1: O sistema deve apresentar um campo para "CPF" quando o cliente for cadastrado como pessoa física e um campo para "CNPJ" quando for pessoa jurídica.
Critério de Aceitação 2.3.2: O sistema deve validar o formato e a validade do CPF inserido (através de algoritmo de validação).
Critério de Aceitação 2.3.3: O sistema deve validar o formato e a validade do CNPJ inserido (através de algoritmo de validação).
Critério de Aceitação 2.3.4: O sistema não deve permitir o cadastro de clientes com CPF ou CNPJ já existentes no sistema.
Como um usuário do sistema, eu quero ser capaz de cadastrar os meios de contato do cliente (telefone principal, telefone secundário opcional, e-mail opcional)...


Critério de Aceitação 2.4.1: O sistema deve apresentar um campo obrigatório para "Telefone Principal" e campos opcionais para "Telefone Secundário" e "E-mail".
Critério de Aceitação 2.4.2: O sistema deve validar o formato do "Telefone Principal" (com DDD).
Critério de Aceitação 2.4.3: O sistema deve validar o formato do "Telefone Secundário" (se preenchido, com DDD).
Critério de Aceitação 2.4.4: O sistema deve validar o formato do "E-mail" (se preenchido).
CRITÉRIO DE ACEITAÇÃO MÓDULO 3: CADASTRO DE VEÍCULOS

# Módulo 3: Cadastro de Veículos 

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo veículo informando o tipo (automóvel ou motocicleta)...


Critério de Aceitação 3.1.1: O sistema deve apresentar um campo de seleção obrigatório para o "Tipo" do veículo, com as opções "Automóvel" e "Motocicleta".
Critério de Aceitação 3.1.2: Ao selecionar o tipo, o sistema pode exibir campos específicos para cada tipo, se necessário (a serem definidos em outras user stories, como número de portas para automóveis).
Como um usuário do sistema, eu quero ser capaz de cadastrar a placa do veículo...


Critério de Aceitação 3.2.1: O sistema deve apresentar um campo obrigatório para a "Placa" do veículo.
Critério de Aceitação 3.2.2: O sistema deve validar o formato da placa (padrão Mercosul ou anterior).
Critério de Aceitação 3.2.3: O sistema não deve permitir o cadastro de veículos com placas já existentes no sistema.
Como um usuário do sistema, eu quero ser capaz de cadastrar a marca e o modelo do veículo...


Critério de Aceitação 3.3.1: O sistema deve apresentar um campo de seleção obrigatório para a "Marca" do veículo, com uma lista de marcas cadastradas (a ser gerenciada em outro módulo, se necessário, ou como uma lista predefinida).
Critério de Aceitação 3.3.2: Após selecionar a "Marca", o sistema deve apresentar um campo de seleção obrigatório para o "Modelo" do veículo, com uma lista de modelos correspondentes à marca selecionada (se aplicável). Caso contrário, um campo de texto livre obrigatório para o modelo.
Como um usuário do sistema, eu quero ser capaz de cadastrar o ano de fabricação do veículo...


Critério de Aceitação 3.4.1: O sistema deve apresentar um campo obrigatório para o "Ano de Fabricação" do veículo.
Critério de Aceitação 3.4.2: O sistema deve validar se o ano de fabricação é um ano válido.
Como um usuário do sistema, eu quero ser capaz de cadastrar a quilometragem atual do veículo...


Critério de Aceitação 3.5.1: O sistema deve apresentar um campo obrigatório para a "Quilometragem Atual" do veículo.
Critério de Aceitação 3.5.2: O sistema deve validar se a quilometragem é um número inteiro positivo.
Como um usuário do sistema, eu quero ser capaz de cadastrar a cor do veículo (opcionalmente)...


Critério de Aceitação 3.6.1: O sistema deve apresentar um campo opcional para a "Cor" do veículo (pode ser um campo de texto livre ou uma lista de cores predefinidas).
Como um usuário do sistema, eu quero ser capaz de adicionar outras informações relevantes sobre o veículo (opcionalmente)...


Critério de Aceitação 3.7.1: O sistema deve apresentar um campo de texto livre opcional para "Outras Informações" ou "Observações" sobre o veículo.

# CRITÉRIOS DE ACEITAÇÃO MÓDULO 4: CADASTRO DE SERVIÇOS

# Módulo 4: Cadastro de Serviços

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo serviço informando um código de serviço único...


Critério de Aceitação 4.1.1: O sistema deve apresentar um campo obrigatório para "Código do Serviço".
Critério de Aceitação 4.1.2: O sistema deve garantir que o código do serviço seja único e não possa ser repetido ao cadastrar novos serviços.
Como um usuário do sistema, eu quero ser capaz de cadastrar o tipo do serviço (ex: Balanceamento, Alinhamento, Reforma de Rodas)...


Critério de Aceitação 4.2.1: O sistema deve apresentar um campo obrigatório para o "Tipo do Serviço" (pode ser um campo de texto livre ou uma lista de tipos predefinidos).
Como um usuário do sistema, eu quero ser capaz de cadastrar uma descrição detalhada do serviço (opcionalmente)...


Critério de Aceitação 4.3.1: O sistema deve apresentar um campo de texto livre opcional para a "Descrição Detalhada" do serviço.
Como um usuário do sistema, eu quero ser capaz de cadastrar o valor unitário do serviço...


Critério de Aceitação 4.4.1: O sistema deve apresentar um campo obrigatório para o "Valor Unitário" do serviço.
Critério de Aceitação 4.4.2: O sistema deve validar se o valor unitário é um número decimal positivo.
Como um usuário do sistema, eu quero ser capaz de cadastrar o tempo médio de execução do serviço (em horas ou minutos)...


Critério de Aceitação 4.5.1: O sistema deve apresentar um campo obrigatório para o "Tempo Médio de Execução".
Critério de Aceitação 4.5.2: O sistema deve permitir a seleção da unidade de tempo ("Horas" ou "Minutos") para o tempo de execução.
Critério de Aceitação 4.5.3: O sistema deve validar se o tempo médio de execução é um número inteiro positivo.
Como um usuário do sistema, eu quero ser capaz de cadastrar a quantidade padrão de rodas envolvidas no serviço (opcionalmente)...


Critério de Aceitação 4.6.1: O sistema deve apresentar um campo opcional para "Quantidade Padrão de Rodas".
Critério de Aceitação 4.6.2: Se preenchido, o sistema deve validar se a quantidade padrão de rodas é um número inteiro positivo.
Como um usuário do sistema, eu quero ser capaz de cadastrar um prazo de entrega padrão para o serviço (opcionalmente, em dias)...


Critério de Aceitação 4.7.1: O sistema deve apresentar um campo opcional para "Prazo de Entrega Padrão (em dias)".
Critério de Aceitação 4.7.2: Se preenchido, o sistema deve validar se o prazo de entrega é um número inteiro positivo.

# CRITÉRIOS DE ACEITAÇÃO MÓDULO 5: ESTOQUE.

# Módulo 5: Estoque

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo produto informando um código único...


Critério de Aceitação 5.1.1: O sistema deve apresentar um campo obrigatório para "Código do Produto".
Critério de Aceitação 5.1.2: O sistema deve garantir que o código do produto seja único e não possa ser repetido ao cadastrar novos produtos.
Como um usuário do sistema, eu quero ser capaz de cadastrar a marca do produto...


Critério de Aceitação 5.2.1: O sistema deve apresentar um campo obrigatório para a "Marca" do produto (pode ser um campo de texto livre ou uma lista de marcas predefinidas).
Como um usuário do sistema, eu quero ser capaz de cadastrar o tipo ou descrição do produto...


Critério de Aceitação 5.3.1: O sistema deve apresentar um campo obrigatório para o "Tipo/Descrição" do produto.
Como um usuário do sistema, eu quero ser capaz de cadastrar outras especificações do produto (opcionalmente)...


Critério de Aceitação 5.4.1: O sistema deve apresentar um campo de texto livre opcional para "Outras Especificações" do produto.
Como um usuário do sistema, eu quero ser capaz de registrar a entrada de novos produtos no estoque, informando a data da entrada...


Critério de Aceitação 5.5.1: O sistema deve apresentar uma funcionalidade para registrar "Entrada de Estoque" com um campo obrigatório para a "Data da Entrada" (com um calendário para seleção).
Como um usuário do sistema, eu quero ser capaz de selecionar o fornecedor do produto na entrada...


Critério de Aceitação 5.6.1: Na tela de "Entrada de Estoque", o sistema deve permitir a seleção de um "Fornecedor" a partir de uma lista de fornecedores cadastrados (a ser gerenciada em outro módulo, se necessário, ou como uma lista predefinida).
Como um usuário do sistema, eu quero ser capaz de informar a quantidade de produtos que estão entrando no estoque...


Critério de Aceitação 5.7.1: Na tela de "Entrada de Estoque", o sistema deve apresentar um campo obrigatório para a "Quantidade" de produtos que estão entrando.
Critério de Aceitação 5.7.2: O sistema deve validar se a quantidade é um número inteiro positivo.
Como um usuário do sistema, eu quero ser capaz de registrar o valor unitário de compra do produto na entrada...


Critério de Aceitação 5.8.1: Na tela de "Entrada de Estoque", o sistema deve apresentar um campo obrigatório para o "Valor Unitário de Compra" do produto.
Critério de Aceitação 5.8.2: O sistema deve validar se o valor unitário de compra é um número decimal positivo.
Como um usuário do sistema, eu quero ser capaz de registrar a saída de produtos do estoque, vinculando-a a um código de venda...


Critério de Aceitação 5.9.1: O sistema deve apresentar uma funcionalidade para registrar "Saída de Estoque" com um campo para vincular ao "Código da Venda" (se aplicável).
Como um usuário do sistema, eu quero ser capaz de registrar a data da saída do produto...


Critério de Aceitação 5.10.1: Na tela de "Saída de Estoque", o sistema deve apresentar um campo obrigatório para a "Data da Saída" (com um calendário para seleção).
Como um usuário do sistema, eu quero ser capaz de informar a quantidade de produtos que estão saindo do estoque...


Critério de Aceitação 5.11.1: Na tela de "Saída de Estoque", o sistema deve apresentar um campo obrigatório para a "Quantidade" de produtos que estão saindo.
Critério de Aceitação 5.11.2: O sistema deve validar se a quantidade é um número inteiro positivo e se há saldo suficiente em estoque para a saída.
Como um usuário do sistema, eu quero que o sistema calcule e exiba o saldo atual de cada produto...


Critério de Aceitação 5.12.1: O sistema deve calcular e exibir o "Saldo Atual" de cada produto, considerando as entradas e saídas registradas.
Critério de Aceitação 5.12.2: O saldo atual deve ser atualizado automaticamente após cada entrada e saída.
Como um usuário do sistema, eu quero ser capaz de definir a capacidade máxima de estocagem para cada produto (opcionalmente)...


Critério de Aceitação 5.13.1: No cadastro do produto, o sistema deve apresentar um campo opcional para "Capacidade Máxima de Estocagem".
Critério de Aceitação 5.13.2: Se preenchido, o sistema deve validar se a capacidade máxima é um número inteiro positivo.
Como um usuário do sistema, eu quero que o sistema me apresente alertas visuais sobre a capacidade de estocagem...


Critério de Aceitação 5.14.1: Se o saldo atual de um produto se aproximar ou exceder a capacidade máxima definida (a definir um limite percentual), o sistema deve exibir um alerta visual (ex: cor diferente, ícone).
Como um usuário do sistema, eu quero ser capaz de definir uma quantidade mínima de estoque para cada produto...


Critério de Aceitação 5.15.1: No cadastro do produto, o sistema deve apresentar um campo obrigatório para "Quantidade Mínima de Estoque".
Critério de Aceitação 5.15.2: O sistema deve validar se a quantidade mínima é um número inteiro positivo.
Como um usuário do sistema, eu quero receber um alerta de compra quando a quantidade em estoque de um produto atingir ou ficar abaixo da quantidade mínima definida...


Critério de Aceitação 5.16.1: O sistema deve gerar um alerta (ex: na tela principal, em um relatório específico) quando o saldo atual de um produto for menor ou igual à sua quantidade mínima definida.
Como um usuário do sistema, eu quero que o sistema calcule e exiba a média de venda diária de cada produto (opcionalmente)...


Critério de Aceitação 5.17.1: O sistema deve oferecer a opção de calcular e exibir a "Média de Venda Diária" para cada produto, com base no histórico de vendas em um período definido (a definir).
Como um usuário do sistema, eu quero que o sistema forneça uma previsão de esgotamento do produto (opcionalmente)...


Critério de Aceitação 5.18.1: O sistema deve oferecer a opção de calcular e exibir uma "Previsão de Esgotamento" para cada produto, com base no saldo atual e na média de venda diária (se disponível).
Como um usuário do sistema, eu quero ser capaz de gerar relatórios dos produtos discriminados pelo ID...


Critério de Aceitação 5.19.1: O sistema deve permitir a geração de um relatório listando os produtos e suas informações (código, marca, tipo, especificações) filtrado por ID.
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do histórico de compras de produtos...


Critério de Aceitação 5.20.1: O sistema deve permitir a geração de um relatório listando as entradas de estoque em um período definido, com detalhes do produto, data, quantidade, valor unitário e fornecedor.
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do histórico de vendas de produtos...


Critério de Aceitação 5.21.1: O sistema deve permitir a geração de um relatório listando as saídas de estoque vinculadas a vendas em um período definido, com detalhes do produto, data, quantidade e código da venda.
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do saldo atual de todos os produtos...


Critério de Aceitação 5.22.1: O sistema deve permitir a geração de um relatório listando todos os produtos cadastrados e seus respectivos saldos atuais.
Como um usuário do sistema, eu quero ser capaz de gerar um relatório de alerta de compra de produtos...


Critério de Aceitação 5.23.1: O sistema deve permitir a geração de um relatório listando os produtos cujo saldo atual atingiu ou está abaixo da quantidade mínima definida.

# CRITÉRIOS DE ACEITAÇÃO MÓDULO 6: CADASTRAR VENDAS

# Módulo 6: Cadastrar Vendas

Como um usuário do sistema, eu quero ser capaz de criar um novo orçamento de serviços e/ou produtos...


Critério de Aceitação 6.1.1: O sistema deve permitir a criação de um novo "Orçamento" com um código único gerado automaticamente.
Critério de Aceitação 6.1.2: O orçamento deve permitir a adição de múltiplos itens, que podem ser tanto serviços quanto produtos.
Como um usuário do sistema, eu quero ser capaz de selecionar o empregado responsável pelo orçamento...


Critério de Aceitação 6.2.1: Ao criar um orçamento, o sistema deve permitir a seleção de um "Empregado Responsável" a partir de uma lista de empregados cadastrados.
Como um usuário do sistema, eu quero ser capaz de definir um prazo de validade para o orçamento (em dias)...


Critério de Aceitação 6.3.1: O sistema deve apresentar um campo para "Prazo de Validade (em dias)" ao criar um orçamento.
Critério de Aceitação 6.3.2: O sistema deve validar se o prazo de validade é um número inteiro positivo.
Como um usuário do sistema, eu quero que o sistema calcule e exiba a data de validade do orçamento automaticamente...


Critério de Aceitação 6.4.1: O sistema deve calcular e exibir a "Data de Validade" do orçamento com base na data de criação e no prazo de validade definido.
Como um usuário do sistema, ao adicionar um item ao orçamento, eu quero ser capaz de especificar se é um produto ou um serviço...


Critério de Aceitação 6.5.1: Ao adicionar um item, o sistema deve permitir a seleção entre "Produto" e "Serviço".
Como um usuário do sistema, ao adicionar um produto ao orçamento, eu quero ser capaz de selecionar o produto...


Critério de Aceitação 6.6.1: Se "Produto" for selecionado, o sistema deve apresentar uma lista de produtos cadastrados para seleção.
Como um usuário do sistema, ao adicionar um produto ao orçamento, eu quero que o sistema calcule o valor bruto total dos produtos e o valor do ICMS...


Critério de Aceitação 6.7.1: Ao adicionar um produto e sua quantidade, o sistema deve calcular o "Valor Bruto Total" (quantidade * valor unitário do produto).
Critério de Aceitação 6.7.2: O sistema deve aplicar a alíquota de ICMS padrão (a ser definida) sobre o valor bruto e exibir o "Valor do ICMS".
Como um usuário do sistema, ao adicionar um serviço ao orçamento, eu quero ser capaz de selecionar o serviço...


Critério de Aceitação 6.8.1: Se "Serviço" for selecionado, o sistema deve apresentar uma lista de serviços cadastrados para seleção.
Como um usuário do sistema, ao adicionar um serviço ao orçamento, eu quero que o sistema calcule o valor bruto total dos serviços e o valor do ISS...


Critério de Aceitação 6.9.1: Ao adicionar um serviço e sua quantidade (geralmente 1), o sistema deve exibir o "Valor Bruto Total" (valor unitário do serviço).
Critério de Aceitação 6.9.2: O sistema deve aplicar a alíquota de ISS padrão (a ser definida) sobre o valor bruto e exibir o "Valor do ISS".
Como um usuário do sistema, eu quero que o sistema calcule o valor total a pagar do orçamento...


Critério de Aceitação 6.10.1: O sistema deve calcular o "Valor Total a Pagar" do orçamento, somando o valor bruto total de produtos e serviços, acrescido dos impostos (ICMS e ISS).
Como um usuário do sistema, eu quero ser capaz de converter um orçamento em uma venda...


Critério de Aceitação 6.11.1: O sistema deve oferecer uma funcionalidade para "Converter Orçamento em Venda".
Critério de Aceitação 6.11.2: Ao converter, o sistema deve manter todos os itens do orçamento original na venda.
Como um usuário do sistema, eu quero que o sistema registre a data da venda automaticamente...


Critério de Aceitação 6.12.1: Ao converter um orçamento em venda, o sistema deve registrar automaticamente a "Data da Venda".
Como um usuário do sistema, ao converter um orçamento em venda, eu quero que o sistema mantenha o código do orçamento original...


Critério de Aceitação 6.13.1: Ao converter um orçamento em venda, o sistema deve manter o "Código do Orçamento Original" para referência.
Critério de Aceitação 6.13.2: A venda também deve receber um novo código único de venda.
Como um usuário do sistema, eu quero que o sistema apresente os valores atualizados dos produtos e serviços na tela de venda...


Critério de Aceitação 6.14.1: Na tela de venda (ao converter um orçamento ou criar uma venda diretamente - se aplicável), o sistema deve exibir os valores unitários atuais dos produtos e serviços cadastrados.
Como um usuário do sistema, eu quero que o sistema calcule o valor total da venda...


Critério de Aceitação 6.15.1: O sistema deve calcular o "Valor Total da Venda", somando os valores dos itens (produtos e serviços) com os impostos aplicáveis.
Como um usuário do sistema, eu quero ser capaz de emitir um relatório de orçamento...


Critério de Aceitação 6.16.1: O sistema deve permitir a geração de um relatório de orçamento que inclua o código do orçamento, data de criação, validade, responsável, lista de itens (com descrição, quantidade, valor unitário, valor total), e valor total do orçamento.
Como um usuário do sistema, ao concluir uma venda, eu quero que o sistema emita automaticamente uma Ordem de Serviço (OS)...


Critério de Aceitação 6.17.1: Ao marcar uma venda como "Concluída", o sistema deve oferecer a opção de gerar automaticamente uma nova Ordem de Serviço (OS) vinculada a essa venda.
Critério de Aceitação 6.17.2: Os itens de serviço da venda devem ser automaticamente incluídos na OS. Os produtos vendidos podem ser listados na OS como "peças utilizadas".
Como um usuário do sistema, eu quero que a Ordem de Serviço gerada possa ser visualizada e impressa...


Critério de Aceitação 6.18.1: O sistema deve permitir a visualização e impressão da Ordem de Serviço gerada.

# CRITÉRIOS DE ACEITAÇÃO MÓDULO 7: CADASTRAR ORDEM DE SERVIÇO

# Módulo 7: Cadastrar Ordem de Serviço

Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada Ordem de Serviço (OS)...


Critério de Aceitação 7.1.1: Ao criar uma nova OS, o sistema deve gerar automaticamente um "Código da OS" único e sequencial.
Como um usuário do sistema, eu quero ser capaz de vincular um ou mais mecânicos responsáveis à Ordem de Serviço...


Critério de Aceitação 7.2.1: Ao criar ou editar uma OS, o sistema deve permitir a seleção de um ou mais "Mecânicos Responsáveis" a partir de uma lista de empregados cadastrados com a função de mecânico (ou similar).
Como um usuário do sistema, eu quero que o sistema registre automaticamente a data e hora de entrada do veículo/serviço na Ordem de Serviço...


Critério de Aceitação 7.3.1: Ao criar uma nova OS, o sistema deve registrar automaticamente a "Data e Hora de Entrada". O usuário também deve ter a opção de editar essa informação, se necessário.
Como um usuário do sistema, eu quero ser capaz de registrar a data e hora de saída (conclusão) do veículo/serviço na Ordem de Serviço...


Critério de Aceitação 7.4.1: O sistema deve permitir o registro da "Data e Hora de Saída" (conclusão) da OS. Esta informação pode ser preenchida manualmente ou automaticamente ao marcar a OS como "Concluída".
Como um usuário do sistema, eu quero ser capaz de vincular um cliente existente à Ordem de Serviço...


Critério de Aceitação 7.5.1: Ao criar uma nova OS, o sistema deve permitir a seleção de um "Cliente" a partir da lista de clientes cadastrados.
Como um usuário do sistema, eu quero ser capaz de adicionar um ou mais produtos utilizados na Ordem de Serviço...


Critério de Aceitação 7.6.1: A OS deve permitir a adição de produtos utilizados, com a possibilidade de selecionar produtos cadastrados no estoque e especificar a quantidade utilizada.
Critério de Aceitação 7.6.2: Ao adicionar um produto, o sistema deve exibir o valor unitário atual do produto (para fins de registro na OS).
Como um usuário do sistema, eu quero ser capaz de adicionar um ou mais serviços realizados na Ordem de Serviço...


Critério de Aceitação 7.7.1: A OS deve permitir a adição de serviços realizados, com a possibilidade de selecionar serviços cadastrados e especificar a quantidade (geralmente 1).
Critério de Aceitação 7.7.2: Ao adicionar um serviço, o sistema deve exibir o valor unitário do serviço.
Como um usuário do sistema, eu quero que a Ordem de Serviço possa ser gerada a partir de uma venda concluída...


Critério de Aceitação 7.8.1: Conforme definido no Módulo 6, ao concluir uma venda, o sistema deve oferecer a opção de gerar uma OS, preenchendo automaticamente os serviços da venda na OS e listando os produtos vendidos como "peças utilizadas". O cliente e o veículo (se cadastrado na venda) também devem ser vinculados à OS.
Como um usuário do sistema, eu quero ser capaz de adicionar observações ou detalhes adicionais à Ordem de Serviço...


Critério de Aceitação 7.9.1: A OS deve conter um campo de texto livre para "Observações" ou "Detalhes Adicionais" sobre o serviço realizado.
Como um usuário do sistema, eu quero que a Ordem de Serviço possa ser visualizada e impressa...


Critério de Aceitação 7.10.1: O sistema deve permitir a visualização da OS com todos os detalhes (código, data/hora de entrada/saída, cliente, veículo, mecânicos, produtos utilizados, serviços realizados, valores, observações).
Critério de Aceitação 7.10.2: O sistema deve permitir a impressão da OS em um formato adequado.

# CRITÉRIOS DE ACEITAÇÃO MÓDULO 8: CADASTRAR FLUXO DE CAIXA

# Módulo 8: Cadastrar Fluxo de Caixa

Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada movimentação de caixa...


Critério de Aceitação 8.1.1: Ao registrar uma nova entrada ou saída, o sistema deve gerar automaticamente um "Código da Movimentação" único e sequencial.
Como um usuário do sistema, eu quero que o sistema registre automaticamente a data da movimentação, mas também me permita inserir uma data manualmente...


Critério de Aceitação 8.2.1: Ao criar uma nova movimentação, o sistema deve preencher automaticamente o campo "Data" com a data atual, mas permitir que o usuário a modifique.
Como um usuário do sistema, eu quero ser capaz de classificar a movimentação como "Entrada" ou "Saída"...


Critério de Aceitação 8.3.1: O sistema deve apresentar um campo de seleção obrigatório para o "Tipo de Movimentação", com as opções "Entrada" e "Saída".
Como um usuário do sistema, ao registrar uma entrada ou saída, eu quero ser capaz de selecionar a forma de pagamento utilizada...


Critério de Aceitação 8.4.1: O sistema deve apresentar um campo de seleção obrigatório para a "Forma de Pagamento" (ex: Dinheiro, Cartão de Crédito, Cartão de Débito, Transferência), com uma lista de formas de pagamento cadastradas (a ser gerenciada em outro módulo, se necessário, ou como uma lista predefinida).
Como um usuário do sistema, eu quero ser capaz de inserir o valor da movimentação...


Critério de Aceitação 8.5.1: O sistema deve apresentar um campo obrigatório para o "Valor" da movimentação.
Critério de Aceitação 8.5.2: O sistema deve validar se o valor é um número decimal positivo.
Como um usuário do sistema, ao registrar uma movimentação, eu quero poder vincular um cliente (opcionalmente)...


Critério de Aceitação 8.6.1: O sistema deve apresentar um campo opcional para vincular um "Cliente" à movimentação, com a possibilidade de selecionar um cliente cadastrado.
Como um usuário do sistema, ao registrar uma movimentação de entrada referente a uma venda, eu quero poder vincular essa movimentação ao código da venda correspondente (opcionalmente)...


Critério de Aceitação 8.7.1: Para movimentações de "Entrada", o sistema deve apresentar um campo opcional para vincular ao "Código da Venda".
Como um usuário do sistema, ao registrar uma movimentação de entrada referente a um serviço concluído, eu quero poder vincular essa movimentação ao código da Ordem de Serviço (OS) correspondente (opcionalmente)...


Critério de Aceitação 8.8.1: Para movimentações de "Entrada", o sistema deve apresentar um campo opcional para vincular ao "Código da OS".
Como um usuário do sistema, eu quero que o sistema registre automaticamente no fluxo de caixa as entradas referentes a vendas de produtos e recebimentos de serviços concluídos...


Critério de Aceitação 8.9.1: Ao marcar uma venda como "Paga" (a ser definido no Módulo 6), o sistema deve gerar automaticamente uma movimentação de "Entrada" no fluxo de caixa, com os detalhes da venda (valor, forma de pagamento, cliente, código da venda).
Critério de Aceitação 8.9.2: Ao marcar uma OS como "Paga" (a ser definido no Módulo 7), o sistema deve gerar automaticamente uma movimentação de "Entrada" no fluxo de caixa, com os detalhes do serviço (valor, forma de pagamento, cliente, código da OS).
Como um usuário do sistema, eu quero que o sistema registre automaticamente no fluxo de caixa as saídas referentes a compras de estoque e pagamentos de fornecedores...


Critério de Aceitação 8.10.1: Ao registrar uma "Entrada de Estoque" com um "Valor Unitário de Compra" (no Módulo 5), o sistema deve oferecer a opção de registrar automaticamente uma movimentação de "Saída" no fluxo de caixa (a ser confirmada pelo usuário).
Critério de Aceitação 8.10.2: O sistema deve permitir o registro de pagamentos a fornecedores (a ser detalhado em outra user story), gerando automaticamente uma movimentação de "Saída" no fluxo de caixa.
Como um usuário do sistema, eu quero ser capaz de registrar manualmente outras entradas e saídas no fluxo de caixa, detalhando a descrição...


Critério de Aceitação 8.11.1: O sistema deve permitir o registro manual de movimentações de "Entrada" e "Saída" com um campo obrigatório para "Descrição" da movimentação.
Como um usuário do sistema, se um pagamento for realizado com cartão de crédito parcelado, eu quero que o sistema agende automaticamente os recebimentos futuros no fluxo de caixa...


Critério de Aceitação 8.12.1: Ao registrar uma "Entrada" com a forma de pagamento "Cartão de Crédito" e indicar um parcelamento (a ser definido), o sistema deve agendar automaticamente as movimentações de entrada futuras no fluxo de caixa, com as datas e valores das parcelas.
Como um usuário do sistema, eu quero ser capaz de gerar um relatório de fechamento diário...


Critério de Aceitação 8.13.1: O sistema deve permitir a geração de um relatório que liste todas as entradas e saídas registradas em um dia específico, com o saldo inicial, total de entradas, total de saídas e saldo final.
Como um usuário do sistema, eu quero ser capaz de gerar um extrato do fluxo de caixa por um período específico...


Critério de Aceitação 8.14.1: O sistema deve permitir a geração de um relatório que liste todas as entradas e saídas registradas dentro de um período selecionado pelo usuário, com o saldo inicial, total de entradas, total de saídas e saldo final para o período.
Como um usuário do sistema, eu quero visualizar um gráfico mostrando a porcentagem de cada forma de pagamento utilizada nas entradas...


Critério de Aceitação 8.15.1: O sistema deve apresentar um gráfico (de pizza ou similar) que mostre a distribuição percentual das formas de pagamento utilizadas nas movimentações de "Entrada" em um período selecionado (pode ser o dia atual, um mês, etc.).

# CRITÉRIOS DE ACEITAÇÃO MÓDULO 9: CADASTRO DE DEPARTAMENTOS

# Módulo 9: Cadastro de Departamentos

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo departamento informando um código único para o departamento...


Critério de Aceitação 9.1.1: O sistema deve apresentar um campo obrigatório para "Código do Departamento".
Critério de Aceitação 9.1.2: O sistema deve garantir que o código do departamento seja único e não possa ser repetido ao cadastrar novos departamentos.
Como um usuário do sistema, ao cadastrar um departamento, eu quero ser capaz de vincular um ou mais empregados a este departamento, especificando o código do empregado e o seu cargo dentro deste departamento...


Critério de Aceitação 9.2.1: Ao cadastrar um departamento, o sistema deve permitir a seleção de um ou mais "Empregados" a partir da lista de empregados cadastrados.
Critério de Aceitação 9.2.2: Para cada empregado vinculado ao departamento, o sistema deve permitir especificar o "Cargo" desse empregado dentro do departamento (ex: Gerente, Supervisor, Técnico).
Como um usuário do sistema, eu quero ser capaz de visualizar os empregados alocados a cada departamento, juntamente com seus respectivos cargos dentro desse departamento...


Critério de Aceitação 9.3.1: O sistema deve permitir a visualização dos detalhes de cada departamento, incluindo a lista de empregados vinculados e seus respectivos cargos.
Como um usuário do sistema, eu quero ser capaz de gerar um relatório geral de todos os departamentos...


Critério de Aceitação 9.4.1: O sistema deve permitir a geração de um relatório listando todos os departamentos cadastrados, com seus códigos e a lista de empregados alocados (com seus cargos).
Como um usuário do sistema, eu quero ser capaz de gerar um relatório específico para um departamento...


Critério de Aceitação 9.5.1: O sistema deve permitir a geração de um relatório para um departamento específico, selecionado pelo usuário, listando todos os empregados alocados e seus respectivos cargos.

# CRITÉRIOS DE ACEITAÇÃO MÓDULO 10: CADASTRO DE EMPREGADOS

# Módulo 10: Cadastro de Empregados

Como um usuário do sistema, eu quero ser capaz de selecionar o departamento ao qual o empregado pertence...


Critério de Aceitação 10.1.1: Ao cadastrar um empregado, o sistema deve apresentar um campo de seleção obrigatório para o "Departamento" ao qual o empregado pertence, com uma lista de departamentos cadastrados.
Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada empregado...


Critério de Aceitação 10.2.1: Ao cadastrar um novo empregado, o sistema deve gerar automaticamente um "Código do Empregado" único e sequencial.
Como um usuário do sistema, eu quero ser capaz de cadastrar o código de dependentes do empregado (opcionalmente)...


Critério de Aceitação 10.3.1: O sistema deve apresentar um campo opcional para "Código de Dependentes" do empregado.
Como um usuário do sistema, eu quero ser capaz de selecionar o cargo do empregado a partir de uma lista predefinida...


Critério de Aceitação 10.4.1: O sistema deve apresentar um campo de seleção obrigatório para o "Cargo" do empregado, com uma lista de cargos predefinidos (a ser gerenciada, se necessário, ou como uma lista fixa).
Como um usuário do sistema, eu quero ser capaz de cadastrar a nacionalidade do empregado...


Critério de Aceitação 10.5.1: O sistema deve apresentar um campo obrigatório para a "Nacionalidade" do empregado (pode ser um campo de texto livre ou uma lista de nacionalidades).
Como um usuário do sistema, eu quero ser capaz de cadastrar a naturalidade do empregado...


Critério de Aceitação 10.6.1: O sistema deve apresentar um campo obrigatório para a "Naturalidade" do empregado (cidade de nascimento).
Como um usuário do sistema, eu quero ser capaz de cadastrar a cidade e a Unidade Federativa (UF) de residência do empregado...


Critério de Aceitação 10.7.1: O sistema deve apresentar campos obrigatórios para a "Cidade de Residência" e a "UF de Residência" (com uma lista de seleção das Unidades Federativas do Brasil).
Como um usuário do sistema, eu quero ser capaz de cadastrar a data de nascimento do empregado...


Critério de Aceitação 10.8.1: O sistema deve apresentar um campo obrigatório para a "Data de Nascimento" do empregado (com um calendário para seleção).
Como um usuário do sistema, eu quero ser capaz de selecionar o estado civil do empregado a partir de uma lista...


Critério de Aceitação 10.9.1: O sistema deve apresentar um campo de seleção obrigatório para o "Estado Civil" do empregado, com uma lista de opções (Solteiro, Casado, Divorciado, Viúvo, etc.)

# DASHBOARDS E RELATÓRIOS GERAIS ESSENCIAIS SIMPLIFICADOS.

# Dashboards Essenciais:

# Dashboard Financeiro Básico:


Saldo Atual do Fluxo de Caixa: Um número que representa o saldo total.
Total de Entradas e Saídas do Dia/Mês: Valores resumidos das movimentações financeiras.
Gráfico Simples de Entradas vs. Saídas (linha ou barra): Uma visualização básica da tendência financeira.

# Dashboard de Vendas Básico:


Total de Vendas do Dia/Mês: Valor total das vendas realizadas.
Top 3 Produtos/Serviços Mais Vendidos: Uma lista dos itens com maior volume de vendas.

# Dashboard de Serviços Básicos:


Total de Serviços Concluídos no Dia/Mês: Número de serviços finalizados.
Número de Serviços Pendentes: Quantidade de serviços ainda em andamento.

# Dashboard de Estoque Básico:


Número de Produtos Abaixo do Estoque Mínimo: Um alerta rápido sobre itens que precisam de reposição.
Valor Total Estimado do Estoque: Uma estimativa do valor do estoque atual.

# PRIORIZAÇÃO ENTRE OS MÓDULOS 

# Prioridade Muito Alta:

Módulo 1: Módulo de Login: Essencial para o acesso seguro ao sistema. Sem ele, nenhum outro módulo pode ser utilizado.

# Prioridade Alta:

Módulo 2: Cadastro de Clientes: Fundamental para começar a registrar informações dos clientes, que são a base do negócio.
Módulo 3: Cadastro de Veículos: Crucial para o negócio de serviços automotivos, pois os serviços estão diretamente ligados aos veículos.
Módulo 4: Cadastro de Serviços: Necessário para definir os serviços que a empresa oferece e que serão utilizados nas vendas e ordens de serviço.

# Prioridade Média:

Módulo 5: Estoque: Importante para gerenciar as peças e produtos utilizados nos serviços e vendas, impactando diretamente a eficiência operacional e os custos.
Módulo 6: Cadastrar Vendas: Permite o registro de orçamentos e vendas, que é a principal fonte de receita. Depende dos cadastros de clientes, veículos e serviços/estoque.
Módulo 7: Cadastrar Ordem de Serviço: Essencial para gerenciar o fluxo de trabalho dos serviços, agendamento e acompanhamento. Depende dos cadastros de clientes, veículos e serviços.

# Prioridade Baixa:

Módulo 8: Cadastrar Fluxo de Caixa: Importante para o controle financeiro, mas pode ser implementado após as funcionalidades principais de operação e receita estarem em funcionamento.
Módulo 9: Cadastro de Departamentos: Útil para a organização interna, mas não diretamente ligado à operação principal do negócio no início.
Módulo 10: Cadastro de Empregados: Fundamental para vincular responsáveis aos processos, mas pode ser implementado gradualmente após os módulos de maior prioridade.

# PRODUCT BACKLOG COM PRIORIZAÇÃO

# Product Backlog Projeto RISO (Atualizado com Priorização)

# Prioridade Muito Alta: 

# Módulo 1: Módulo de Login

Como um usuário, eu quero poder realizar login no sistema para acessar minhas funcionalidades e dados de forma segura. (Critérios de Aceitação Detalhados)
Como um usuário, eu quero poder inserir meu nome de usuário e senha para me autenticar no sistema. (Critérios de Aceitação Detalhados)
Como um usuário, eu quero ser notificado caso minhas credenciais estejam incorretas para poder tentar novamente. (Critérios de Aceitação Detalhados)
Como um usuário, eu quero ter a opção de "lembrar meu usuário" para facilitar logins futuros (se aplicável). (Critérios de Aceitação Detalhados)
Como um usuário, eu quero ter a opção de "esqueci minha senha" para poder recuperá-la caso necessário. (Critérios de Aceitação Detalhados)
Como um administrador, eu quero poder gerenciar os usuários do sistema (criar, editar, desativar). (Critérios de Aceitação Detalhados)
Como um administrador, eu quero poder definir os níveis de acesso para diferentes tipos de usuários. (Critérios de Aceitação Detalhados)

# Prioridade Alta: 

# Módulo 2: Cadastro de Clientes

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo cliente informando seu nome completo ou razão social... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o endereço do cliente (CEP, rua, número, complemento, bairro, cidade, estado)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o CPF para clientes pessoa física e o CNPJ para clientes pessoa jurídica... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar os meios de contato do cliente (telefone principal, telefone secundário opcional, e-mail opcional)... (Critérios de Aceitação Detalhados)

# Módulo 3: Cadastro de Veículos

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo veículo informando o tipo (automóvel ou motocicleta)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar a placa do veículo... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar a marca e o modelo do veículo... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o ano de fabricação do veículo... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar a quilometragem atual do veículo... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar a cor do veículo (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de adicionar outras informações relevantes sobre o veículo (opcionalmente)... (Critérios de Aceitação Detalhados)

# Módulo 4: Cadastro de Serviços

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo serviço informando um código de serviço único... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o tipo do serviço (ex: Balanceamento, Alinhamento, Reforma de Rodas)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar uma descrição detalhada do serviço (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o valor unitário do serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o tempo médio de execução do serviço (em horas ou minutos)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar a quantidade padrão de rodas envolvidas no serviço (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar um prazo de entrega padrão para o serviço (opcionalmente, em dias)... (Critérios de Aceitação Detalhados)

# Prioridade Média: 

# Módulo 5: Estoque

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo produto informando um código único... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar a marca do produto... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o tipo ou descrição do produto... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar outras especificações do produto (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de registrar a entrada de novos produtos no estoque, informando a data da entrada... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de selecionar o fornecedor do produto na entrada... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de informar a quantidade de produtos que estão entrando no estoque... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de registrar o valor unitário de compra do produto na entrada... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de registrar a saída de produtos do estoque, vinculando-a a um código de venda... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de registrar a data da saída do produto... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de informar a quantidade de produtos que estão saindo do estoque... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema calcule e exiba o saldo atual de cada produto... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de definir a capacidade máxima de estocagem para cada produto (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema me apresente alertas visuais sobre a capacidade de estocagem... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de definir uma quantidade mínima de estoque para cada produto... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero receber um alerta de compra quando a quantidade em estoque de um produto atingir ou ficar abaixo da quantidade mínima definida... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema calcule e exiba a média de venda diária de cada produto (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema forneça uma previsão de esgotamento do produto (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar relatórios dos produtos discriminados pelo ID... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do histórico de compras de produtos... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do histórico de vendas de produtos... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório do saldo atual de todos os produtos... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório de alerta de compra de produtos... (Critérios de Aceitação Detalhados)

# Módulo 6: Cadastrar Vendas

Como um usuário do sistema, eu quero ser capaz de criar um novo orçamento de serviços e/ou produtos... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de selecionar o empregado responsável pelo orçamento... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de definir um prazo de validade para o orçamento (em dias)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema calcule e exiba a data de validade do orçamento automaticamente... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao adicionar um item ao orçamento, eu quero ser capaz de especificar se é um produto ou um serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao adicionar um produto ao orçamento, eu quero ser capaz de selecionar o produto... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao adicionar um produto ao orçamento, eu quero que o sistema calcule o valor bruto total dos produtos e o valor do ICMS... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao adicionar um serviço ao orçamento, eu quero ser capaz de selecionar o serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao adicionar um serviço ao orçamento, eu quero que o sistema calcule o valor bruto total dos serviços e o valor do ISS... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema calcule o valor total a pagar do orçamento... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de converter um orçamento em uma venda... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema registre a data da venda automaticamente... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao converter um orçamento em venda, eu quero que o sistema mantenha o código do orçamento original... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema apresente os valores atualizados dos produtos e serviços na tela de venda... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema calcule o valor total da venda... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de emitir um relatório de orçamento... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao concluir uma venda, eu quero que o sistema emita automaticamente uma Ordem de Serviço (OS)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que a Ordem de Serviço gerada possa ser visualizada e impressa... (Critérios de Aceitação Detalhados)

# Módulo 7: Cadastrar Ordem de Serviço

Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada Ordem de Serviço (OS)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de vincular um ou mais mecânicos responsáveis à Ordem de Serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema registre automaticamente a data e hora de entrada do veículo/serviço na Ordem de Serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de registrar a data e hora de saída (conclusão) do veículo/serviço na Ordem de Serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de vincular um cliente existente à Ordem de Serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de adicionar um ou mais produtos utilizados na Ordem de Serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de adicionar um ou mais serviços realizados na Ordem de Serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que a Ordem de Serviço possa ser gerada a partir de uma venda concluída... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de adicionar observações ou detalhes adicionais à Ordem de Serviço... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que a Ordem de Serviço possa ser visualizada e impressa... (Critérios de Aceitação Detalhados)
# Prioridade Baixa: 

# Módulo 8: Cadastrar Fluxo de Caixa

Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada movimentação de caixa... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema registre automaticamente a data da movimentação, mas também me permita inserir uma data manualmente... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de classificar a movimentação como "Entrada" ou "Saída"... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao registrar uma entrada ou saída, eu quero ser capaz de selecionar a forma de pagamento utilizada... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de inserir o valor da movimentação... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao registrar uma movimentação, eu quero poder vincular um cliente (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao registrar uma movimentação de entrada referente a uma venda, eu quero poder vincular essa movimentação ao código da venda correspondente (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao registrar uma movimentação de entrada referente a um serviço concluído, eu quero poder vincular essa movimentação ao código da Ordem de Serviço (OS) correspondente (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema registre automaticamente no fluxo de caixa as entradas referentes a vendas de produtos e recebimentos de serviços concluídos... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema registre automaticamente no fluxo de caixa as saídas referentes a compras de estoque e pagamentos de fornecedores... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de registrar manualmente outras entradas e saídas no fluxo de caixa, detalhando a descrição... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, se um pagamento for realizado com cartão de crédito parcelado, eu quero que o sistema agende automaticamente os recebimentos futuros no fluxo de caixa... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório de fechamento diário... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um extrato do fluxo de caixa por um período específico... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero visualizar um gráfico mostrando a porcentagem de cada forma de pagamento utilizada nas entradas... (Critérios de Aceitação Detalhados)

# Módulo 9: Cadastro de Departamentos

Como um usuário do sistema, eu quero ser capaz de cadastrar um novo departamento informando um código único para o departamento... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, ao cadastrar um departamento, eu quero ser capaz de vincular um ou mais empregados a este departamento, especificando o código do empregado e o seu cargo dentro deste departamento... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de visualizar os empregados alocados a cada departamento, juntamente com seus respectivos cargos dentro desse departamento... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório geral de todos os departamentos... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de gerar um relatório específico para um departamento... (Critérios de Aceitação Detalhados)
Módulo 10: Cadastro de Empregados
Como um usuário do sistema, eu quero ser capaz de selecionar o departamento ao qual o empregado pertence... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero que o sistema gere automaticamente um código único para cada empregado... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar o código de dependentes do empregado (opcionalmente)... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de selecionar o cargo do empregado a partir de uma lista predefinida... (Critérios de Aceitação Detalhados)
Como um usuário do sistema, eu quero ser capaz de cadastrar.
## PRODUCT BACKLOG COM PRIORIDADES RESUMIDO

# Product Backlog Projeto RISO (Atualizado com Novas Prioridades)

# Prioridade Muito Alta:

Módulo 1: Módulo de Login (Critérios de Aceitação Detalhados)
Prioridade Alta:
Módulo 2: Cadastro de Clientes (Critérios de Aceitação Detalhados)
Módulo 3: Cadastro de Veículos (Critérios de Aceitação Detalhados)
Módulo 4: Cadastro de Serviços (Critérios de Aceitação Detalhados)
Prioridade Média:
Módulo 5: Estoque (Critérios de Aceitação Detalhados)
Módulo 6: Cadastrar Vendas (Critérios de Aceitação Detalhados)
Módulo 7: Cadastrar Ordem de Serviço (Critérios de Aceitação Detalhados)
Prioridade Baixa:
Módulo 8: Cadastrar Fluxo de Caixa (Critérios de Aceitação Detalhados)
Módulo 9: Cadastro de Departamentos (Critérios de Aceitação Detalhados)
Módulo 10: Cadastro de Empregados (Critérios de Aceitação Detalhados)

# DASHBOARDS E RELATÓRIOS GERAIS ESSENCIAIS SIMPLIFICADOS.

Dashboards Essenciais:
Dashboard Financeiro Básico:


Saldo Atual do Fluxo de Caixa: Um número que representa o saldo total.
Total de Entradas e Saídas do Dia/Mês: Valores resumidos das movimentações financeiras.
Gráfico Simples de Entradas vs. Saídas (linha ou barra): Uma visualização básica da tendência financeira.
Dashboard de Vendas Básico:


Total de Vendas do Dia/Mês: Valor total das vendas realizadas.
Top 3 Produtos/Serviços Mais Vendidos: Uma lista dos itens com maior volume de vendas.
Dashboard de Serviços Básicos:


Total de Serviços Concluídos no Dia/Mês: Número de serviços finalizados.
Número de Serviços Pendentes: Quantidade de serviços ainda em andamento.
Dashboard de Estoque Básico:


Número de Produtos Abaixo do Estoque Mínimo: Um alerta rápido sobre itens que precisam de reposição.
Valor Total Estimado do Estoque: Uma estimativa do valor do estoque atual.

# CONCLUSÃO

Este é o projeto inicial do Product Backlog do Projeto RISO que está sendo apresentado pelo Product Owner (PO) para a Equipe de Desenvolvimento.
Em metodologias ágeis, como o Scrum, que é uma abordagem comum para o desenvolvimento de software flexível, o Product Backlog é considerado um artefato vivo e dinâmico, e pode ser modificado pela Equipe de Desenvolvedores e pelos Stakeholders, em razão de alguns motivos, especialmente os seguintes, conforme consta da literatura, ao longo do desenvolvimento.

Aqui estão os principais motivos pelos quais o Product Backlog é modificado ao longo do desenvolvimento:

Novas Descobertas e Requisitos: À medida que a equipe de desenvolvimento trabalha no sistema e obtém feedback dos stakeholders ou usuários, novas necessidades, funcionalidades ou melhorias podem surgir. Essas novas ideias precisam ser adicionadas ao backlog.

Mudanças nas Prioridades do Negócio: As prioridades do negócio podem mudar devido a fatores como mudanças no mercado, ações da concorrência, novas oportunidades ou restrições orçamentárias. Isso pode levar à reordenação ou remoção de itens do backlog.

Feedback dos Usuários e Stakeholders: O feedback contínuo dos usuários e stakeholders é crucial. Esse feedback pode revelar que certas funcionalidades não atendem às expectativas, precisam de ajustes ou que outras funcionalidades são mais importantes do que se pensava inicialmente.
Aprendizado da Equipe de Desenvolvimento: Durante o desenvolvimento, a equipe pode aprender mais sobre os desafios técnicos, as dependências entre os itens do backlog ou encontrar maneiras mais eficientes de implementar certas funcionalidades. Isso pode levar a alterações na forma como os itens do backlog são definidos ou priorizados.

Refinamento Contínuo do Backlog (Product Backlog Refinement): Em muitas metodologias ágeis, há cerimônias regulares de refinamento do backlog. Nessas reuniões, o Product Owner, a equipe de desenvolvimento e outros stakeholders revisam os itens do backlog, adicionam detalhes, estimativas, dividem itens grandes em menores e reavaliam a priorização.

O Product Owner é o principal responsável por gerenciar e manter o Product Backlog. Ele é quem decide quais itens entram no backlog, qual a prioridade deles e quem garante que o backlog esteja claro e compreensível para a equipe de desenvolvimento. No entanto, a modificação do backlog é frequentemente um esforço colaborativo que envolve a equipe de desenvolvimento e outros stakeholders.