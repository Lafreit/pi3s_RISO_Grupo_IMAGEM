// src/services/api.js

// Define a URL base da sua API Django.
// É crucial que esta URL esteja correta e aponte para o seu backend Django.
const API_BASE_URL = 'http://127.0.0.1:8000/api/';

/**
 * Função auxiliar para fazer requisições HTTP para a API Django.
 * Inclui automaticamente o token JWT se disponível no localStorage.
 *
 * @param {string} path O endpoint específico da API (ex: 'servicos/', 'clientes/').
 * @param {object} options Opções de configuração para a requisição fetch (method, body, etc.).
 * @returns {Promise<object>} Os dados JSON da resposta da API.
 * @throws {Error} Lança um erro se a requisição falhar ou a resposta não for JSON esperada.
 */
export const apiRequest = async (path, options = {}) => {
  // Tenta obter o token de acesso do armazenamento local do navegador.
  const token = localStorage.getItem('access_token');

  // Prepara os cabeçalhos da requisição.
  const headers = {
    'Content-Type': 'application/json', // Informa ao servidor que estamos enviando/esperando JSON
    ...options.headers, // Permite sobrescrever ou adicionar outros cabeçalhos
  };

  // Se um token for encontrado, adicione-o ao cabeçalho de Autorização.
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
    console.log('API Request: Token de autorização adicionado ao cabeçalho.');
  } else {
    console.log('API Request: Nenhum token de autorização encontrado. Fazendo requisição pública.');
  }

  // Constrói a URL completa da requisição usando template literals (crases ` `).
  const url = `${API_BASE_URL}${path}`;
  console.log('API Request: Fazendo requisição para:', url);
  console.log('API Request: Cabeçalhos da requisição:', headers);

  try {
    // Realiza a requisição fetch.
    const response = await fetch(url, {
      ...options, // Espalha as opções passadas (method, body, etc.)
      headers: headers, // Aplica os cabeçalhos construídos
    });

    console.log('API Request: Resposta recebida. Status:', response.status, response.statusText);

    // Lemos a resposta como texto primeiro para lidar com erros não-JSON.
    const responseText = await response.text();
    console.log('API Request: Conteúdo RAW da resposta:', responseText.substring(0, 500) + (responseText.length > 500 ? '...' : '')); // Limita para não poluir o console

    // Lógica para tratar respostas de erro (HTTP status não-2xx).
    // Se o status for 401 e não for a rota de login (indicando token expirado/inválido para rota protegida).
    if (response.status === 401 && path !== 'autenticacao/login/') {
      console.warn('API Request: Token expirado ou inválido (401). Limpando tokens e redirecionando para login.');
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      window.location.href = '/login'; // Redireciona o navegador
      return null; // Interrompe o fluxo da função
    }

    // Se a resposta NÃO foi OK (status 4xx ou 5xx).
    if (!response.ok) {
      try {
        // Tenta parsear o texto de erro como JSON, caso o backend envie erros em JSON.
        const errorData = JSON.parse(responseText);
        throw new Error(errorData.detail || errorData.message || JSON.stringify(errorData) || `Erro da API: ${response.status} ${response.statusText}`);
      } catch (parseError) {
        // Se o erro não for JSON (ex: HTML de erro), lança o texto bruto.
        throw new Error(`Erro da API (${response.status} ${response.statusText}): Resposta não JSON. Conteúdo: ${responseText.substring(0, 200)}...`);
      }
    }

    // Se a resposta foi OK (status 2xx), tenta parsear como JSON.
    try {
      return JSON.parse(responseText);
    } catch (jsonParseError) {
      // Erro ao parsear JSON mesmo com status OK (resposta vazia, malformada).
      console.error('API Request: Erro ao parsear JSON de resposta OK:', jsonParseError);
      throw new Error(`Erro ao parsear JSON (Status OK): ${jsonParseError.message}. Conteúdo recebido: ${responseText.substring(0, 200)}...`);
    }

  } catch (error) {
    // Captura erros de rede ou erros lançados pelos blocos try/catch internos.
    console.error('Erro na requisição da API (catch final):', error);
    throw error; // Propaga o erro para o componente que chamou apiRequest
  }
};