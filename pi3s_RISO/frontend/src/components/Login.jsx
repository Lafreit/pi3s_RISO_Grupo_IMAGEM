// src/components/Login.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // <-- Importe useNavigate
import './Login.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate(); // <-- Hook para navegação programática

  const handleSubmit = async (event) => {
    event.preventDefault();
    setMessage('Tentando fazer login...');

    const API_URL = 'http://127.0.0.1:8000/api/autenticacao/login/';

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: username,
          password: password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage('Login bem-sucedido!');
        console.log('Tokens recebidos:', data);

        // 1. Armazenar os tokens no localStorage
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);
        console.log('Tokens armazenados no localStorage.');

        // 2. Redirecionar o usuário para a página inicial (Home)
        navigate('/'); // Redireciona para a rota "/"
      } else {
        setMessage(`Erro no login: ${data.detail || JSON.stringify(data)}`);
        console.error('Erro na resposta da API:', data);
      }
    } catch (error) {
      setMessage(`Erro de conexão: ${error.message}. Verifique se o backend está rodando.`);
      console.error('Erro ao conectar ao servidor:', error);
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">Nome de Usuário:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Senha:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Entrar</button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default Login;