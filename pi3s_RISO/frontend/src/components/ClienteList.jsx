// src/components/ClienteList.jsx
import React, { useState, useEffect } from 'react';
import { apiRequest } from '../services/api';
import { Link } from 'react-router-dom'; // <-- Importe Link
import './ClienteList.css';

function ClienteList() {
    const [clientes, setClientes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchClientes = async () => {
            try {
                setLoading(true);
                setError(null);
                // Usamos 'clientes/clientes/' pois é o padrão para ViewSets no DRF
                // se o API Root estiver em /api/clientes/
                const data = await apiRequest('clientes/clientes/');

                if (Array.isArray(data)) {
                    setClientes(data);
                } else {
                    // Se a API retornar um objeto ou outro formato, logamos para depurar
                    console.warn("Resposta da API de clientes não é um array:", data);
                    setError("Formato de dados inesperado da API de clientes.");
                    setClientes([]); // Garante que clientes seja um array vazio
                }
            } catch (err) {
                console.error("Erro ao buscar clientes:", err);
                setError(err.message || "Ocorreu um erro ao carregar os clientes.");
                setClientes([]);
            } finally {
                setLoading(false);
            }
        };

        fetchClientes();
    }, []); // O array vazio garante que o efeito só rode uma vez, ao montar o componente

    if (loading) {
        return <div className="cliente-list-container">Carregando clientes...</div>;
    }

    if (error) {
        return <div className="cliente-list-container error-message">Erro: {error}</div>;
    }

    return (
        <div className="cliente-list-container">
            <h2>Lista de Clientes</h2>
            {/* Botão para Novo Cliente */}
            <div className="cliente-list-actions"> {/* Adicione esta div para organizar */}
                <Link to="/clientes/novo" className="add-cliente-button">
                    Novo Cliente
                </Link>
            </div>

            {clientes.length === 0 ? (
                <p>Nenhum cliente cadastrado ainda.</p>
            ) : (
                <table className="cliente-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome Completo</th>
                            <th>Email</th>
                            <th>Telefone</th>
                            <th>CPF/CNPJ</th>
                            {/* Adicione mais colunas conforme seus campos do modelo Cliente */}
                        </tr>
                    </thead>
                    <tbody>
                        {clientes.map(cliente => (
                            <tr key={cliente.id}>
                                <td>{cliente.id}</td>
                                <td>{cliente.nome_completo_razao_social}</td>
                                <td>{cliente.email}</td>
                                <td>{cliente.telefone_principal}</td>
                                <td>{cliente.cpf || cliente.cnpj}</td>
                                {/* Adicione mais células conforme seus campos */}
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
}

export default ClienteList;