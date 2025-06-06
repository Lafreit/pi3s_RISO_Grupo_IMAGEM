graph TD
    subgraph Prioridade Muito Alta
        A[#1 Módulo de Login]
    end

    subgraph Prioridade Alta
        B[#2 Cadastro de Clientes]
        C[#3 Cadastro de Veículos]
        D[#4 Cadastro de Serviços]
        E[#7 Cadastrar Ordem de Serviço]
    end

    subgraph Prioridade Média
        F[#5 Estoque]
        G[#6 Cadastrar Vendas]
    end

    subgraph Prioridade Baixa
        H[#8 Cadastrar Fluxo de Caixa]
        I[#9 Cadastro de Departamentos]
        J[#10 Cadastro de Empregados]
    end

    A --> B
    A --> C
    A --> D
    A --> E

    B --> G
    C --> G
    D --> G

    D --> F
    F --> G

    B --> E
    C --> E
    D --> E

    G --> H
    E --> H
    ```