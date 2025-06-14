// src/components/Home.jsx
import React, { useState, useEffect } from 'react';
import { apiRequest } from '../services/api';
import { useNavigate } from 'react-router-dom'; // <-- Importe useNavigate para redirecionamento
import './Home.css';

function Home() {
  const [apiMessage, setApiMessage] = useState('Carregando dados da API...');
  const [servicos, setServicos] = useState([]);
  const navigate = useNavigate(); // <-- Hook para navegação programática

  useEffect(() => {
    console.log('Componente Home carregado. Tentando buscar serviços...');

    const fetchServicos = async () => {
      try {
        const data = await apiRequest('servicos/');

        if (data && Array.isArray(data)) {
          if (data.length > 0) {
            setServicos(data);
            setApiMessage(`Dados de serviços carregados com sucesso! Total: ${data.length} serviços.`);
          } else {
            setApiMessage('API acessada com sucesso, mas nenhum serviço encontrado.');
            setServicos([]);
          }
        } else {
          setApiMessage('API acessada com sucesso, mas o formato da resposta de serviços não é o esperado.');
          setServicos([]);
        }
      } catch (error) {
        setApiMessage(`Erro ao buscar serviços: ${error.message}`);
      }
    };

    fetchServicos();
  }, []);

  // Função para lidar com o logout
  const handleLogout = () => {
    localStorage.removeItem('access_token'); // Remove o token de acesso
    localStorage.removeItem('refresh_token'); // Remove o token de refresh
    console.log('Tokens JWT removidos do localStorage. Usuário deslogado.');
    navigate('/login'); // Redireciona para a página de login
  };

  return (
    <div className="home-container">
      <div className="home-header"> {/* Adicione um container para o título e o botão */}
        <h2>Página Inicial do Sistema</h2>
        <button className="logout-button" onClick={handleLogout}>Sair</button> {/* Botão de Logout */}
      </div>
      <p>Este é o seu primeiro componente React isolado e será a base para a navegação.</p>
      <hr />
      <h3>Status da Conexão com a API (Serviços):</h3>
      <p><strong>{apiMessage}</strong></p>

      {servicos.length > 0 && (
  <div>
    <h4>Lista de Serviços (Requisição Autenticada):</h4>
    <ul>
      {servicos.map(servico => (
        <li key={servico.id}>
          {/* Use os nomes exatos do seu JSON */}
          <strong>{servico.codigo_servico}</strong>: {servico.descricao_detalhada} (Preço: R$ {servico.valor_unitario ? servico.valor_unitario.replace('.', ',') : 'N/A'})
          {/* Adicionei uma verificação servico.valor_unitario? para evitar erro se for nulo/undefined */}
        </li>
      ))}
    </ul>
  </div>
)}
    </div>
  );
}

export default Home;