// src/components/ClienteForm.jsx
import React, { useState, useEffect } from 'react';
import { apiRequest } from '../services/api';
import { useNavigate, useParams } from 'react-router-dom'; // Importe useParams
import './ClienteForm.css';

function ClienteForm() {
    const [formData, setFormData] = useState({
        tipo_cliente: 'PF', // Valor padrão
        nome_completo_razao_social: '',
        cpf: '',
        cnpj: '',
        cep: '',
        rua: '',
        numero: '',
        complemento: '',
        bairro: '',
        cidade: '',
        estado: '',
        telefone_principal: '',
        telefone_secundario: '',
        email: '',
        ativo: true,
    });
    const [message, setMessage] = useState('');
    const [isEditing, setIsEditing] = useState(false); // Novo estado para controlar edição
    const navigate = useNavigate();
    const { id } = useParams(); // Hook para pegar o ID da URL se estiver em modo de edição

    useEffect(() => {
        if (id) {
            setIsEditing(true);
            const fetchCliente = async () => {
                try {
                    // Buscar os dados do cliente para preencher o formulário
                    const data = await apiRequest(`clientes/clientes/${id}/`);
                    setFormData(data);
                    setMessage('');
                } catch (error) {
                    console.error("Erro ao carregar cliente para edição:", error);
                    setMessage(`Erro ao carregar cliente: ${error.message}`);
                }
            };
            fetchCliente();
        }
    }, [id]); // Dependência no 'id' para recarregar se o ID da URL mudar

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        let newValue = type === 'checkbox' ? checked : value;
        // Limpa CPF e CNPJ de caracteres não numéricos antes de salvar no estado
    if (name === 'cpf' || name === 'cnpj') {
        newValue = newValue.replace(/\D/g, ''); // Remove tudo que não for dígito
    }
        setFormData(prevData => ({
            ...prevData,
            [name]: newValue
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('Salvando cliente...');

        const method = isEditing ? 'PUT' : 'POST';
        const endpoint = isEditing ? `clientes/clientes/${id}/` : 'clientes/clientes/';

        try {
            const data = await apiRequest(endpoint, {
                method: method,
                body: JSON.stringify(formData)
            });
            setMessage(`Cliente ${isEditing ? 'atualizado' : 'cadastrado'} com sucesso!`);
            console.log('Resposta da API:', data);

            // Opcional: Redirecionar para a lista de clientes após salvar
            setTimeout(() => {
                navigate('/clientes');
            }, 1500); 

        } catch (error) {
            console.error("Erro ao salvar cliente:", error);
            setMessage(`Erro ao salvar cliente: ${error.message}`);
        }
    };

    return (
        <div className="cliente-form-container">
            <h2>{isEditing ? 'Editar Cliente' : 'Cadastrar Novo Cliente'}</h2>
            <form onSubmit={handleSubmit}>
                {/* Tipo de Cliente (PF/PJ) */}
                <div className="form-group">
                    <label htmlFor="tipo_cliente">Tipo de Cliente:</label>
                    <select
                        id="tipo_cliente"
                        name="tipo_cliente"
                        value={formData.tipo_cliente}
                        onChange={handleChange}
                        required
                    >
                        <option value="PF">Pessoa Física</option>
                        <option value="PJ">Pessoa Jurídica</option>
                    </select>
                </div>

                {/* Nome Completo / Razão Social */}
                <div className="form-group">
                    <label htmlFor="nome_completo_razao_social">{formData.tipo_cliente === 'PF' ? 'Nome Completo:' : 'Razão Social:'}</label>
                    <input
                        type="text"
                        id="nome_completo_razao_social"
                        name="nome_completo_razao_social"
                        value={formData.nome_completo_razao_social}
                        onChange={handleChange}
                        required
                    />
                </div>

                {/* CPF (somente se PF) */}
                {formData.tipo_cliente === 'PF' && (
                    <div className="form-group">
                        <label htmlFor="cpf">CPF:</label>
                        <input
                            type="text"
                            id="cpf"
                            name="cpf"
                            value={formData.cpf}
                            onChange={handleChange}
                            placeholder="Ex: 123.456.789-00"
                            required={formData.tipo_cliente === 'PF'}
                        />
                    </div>
                )}

                {/* CNPJ (somente se PJ) */}
                {formData.tipo_cliente === 'PJ' && (
                    <div className="form-group">
                        <label htmlFor="cnpj">CNPJ:</label>
                        <input
                            type="text"
                            id="cnpj"
                            name="cnpj"
                            value={formData.cnpj}
                            onChange={handleChange}
                            placeholder="Ex: 12.345.678/0001-90"
                            required={formData.tipo_cliente === 'PJ'}
                        />
                    </div>
                )}

                {/* Email */}
                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>

                {/* Telefone Principal */}
                <div className="form-group">
                    <label htmlFor="telefone_principal">Telefone Principal:</label>
                    <input
                        type="text"
                        id="telefone_principal"
                        name="telefone_principal"
                        value={formData.telefone_principal}
                        onChange={handleChange}
                        placeholder="Ex: (XX) 9XXXX-XXXX"
                        required
                    />
                </div>

                {/* Telefone Secundário (Opcional) */}
                <div className="form-group">
                    <label htmlFor="telefone_secundario">Telefone Secundário:</label>
                    <input
                        type="text"
                        id="telefone_secundario"
                        name="telefone_secundario"
                        value={formData.telefone_secundario}
                        onChange={handleChange}
                        placeholder="Ex: (XX) XXXX-XXXX"
                    />
                </div>

                {/* CEP */}
                <div className="form-group">
                    <label htmlFor="cep">CEP:</label>
                    <input
                        type="text"
                        id="cep"
                        name="cep"
                        value={formData.cep}
                        onChange={handleChange}
                        placeholder="Ex: 12345-678"
                        required
                    />
                </div>

                {/* Rua */}
                <div className="form-group">
                    <label htmlFor="rua">Rua:</label>
                    <input
                        type="text"
                        id="rua"
                        name="rua"
                        value={formData.rua}
                        onChange={handleChange}
                        required
                    />
                </div>

                {/* Número */}
                <div className="form-group">
                    <label htmlFor="numero">Número:</label>
                    <input
                        type="text"
                        id="numero"
                        name="numero"
                        value={formData.numero}
                        onChange={handleChange}
                        required
                    />
                </div>

                {/* Complemento (Opcional) */}
                <div className="form-group">
                    <label htmlFor="complemento">Complemento:</label>
                    <input
                        type="text"
                        id="complemento"
                        name="complemento"
                        value={formData.complemento}
                        onChange={handleChange}
                    />
                </div>

                {/* Bairro */}
                <div className="form-group">
                    <label htmlFor="bairro">Bairro:</label>
                    <input
                        type="text"
                        id="bairro"
                        name="bairro"
                        value={formData.bairro}
                        onChange={handleChange}
                        required
                    />
                </div>

                {/* Cidade */}
                <div className="form-group">
                    <label htmlFor="cidade">Cidade:</label>
                    <input
                        type="text"
                        id="cidade"
                        name="cidade"
                        value={formData.cidade}
                        onChange={handleChange}
                        required
                    />
                </div>

                {/* Estado */}
                <div className="form-group">
                    <label htmlFor="estado">Estado (UF):</label>
                    <input
                        type="text"
                        id="estado"
                        name="estado"
                        value={formData.estado}
                        onChange={handleChange}
                        maxLength="2"
                        placeholder="Ex: SP"
                        required
                    />
                </div>

                {/* Ativo (Checkbox) */}
                <div className="form-group checkbox-group">
                    <input
                        type="checkbox"
                        id="ativo"
                        name="ativo"
                        checked={formData.ativo}
                        onChange={handleChange}
                    />
                    <label htmlFor="ativo">Cliente Ativo</label>
                </div>

                <button type="submit">
                    {isEditing ? 'Atualizar Cliente' : 'Cadastrar Cliente'}
                </button>
            </form>
            {message && <p className={`message ${message.includes('Erro') ? 'error' : 'success'}`}>{message}</p>}
        </div>
    );
}

export default ClienteForm;