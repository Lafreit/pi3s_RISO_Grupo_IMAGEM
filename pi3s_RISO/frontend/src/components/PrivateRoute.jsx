// src/components/PrivateRoute.jsx
import React from 'react';
import { Navigate } from 'react-router-dom'; // Importa Navigate para redirecionar

/**
 * Componente para proteger rotas.
 * Redireciona para a página de login se o usuário não estiver autenticado.
 * @param {object} props - Propriedades do componente.
 * @param {React.ReactNode} props.children - Os componentes filhos que serão renderizados se o usuário estiver autenticado.
 */
function PrivateRoute({ children }) {
  // Verifica se existe um token de acesso no localStorage
  const isAuthenticated = localStorage.getItem('access_token');

  // Se não estiver autenticado, redireciona para a página de login
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />; // 'replace' impede que o usuário volte para a rota protegida com o botão "Voltar" do navegador
  }

  // Se estiver autenticado, renderiza os componentes filhos
  return children;
}

export default PrivateRoute;