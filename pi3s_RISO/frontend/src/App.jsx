// src/App.jsx
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Home from './components/Home';
import PrivateRoute from './components/PrivateRoute';
import ClienteList from './components/ClienteList';
import ClienteForm from './components/ClienteForm'; // <-- Importe ClienteForm

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Rota para a página de Login - esta deve ser sempre pública */}
          <Route path="/login" element={<Login />} />

          {/* Rota para a Página Inicial (Home) - PROTEGIDA */}
          <Route 
            path="/" 
            element={
              <PrivateRoute>
                <Home />
              </PrivateRoute>
            } 
          /> 

          {/* Rota para a Lista de Clientes - PROTEGIDA */}
          <Route 
            path="/clientes" 
            element={
              <PrivateRoute>
                <ClienteList />
              </PrivateRoute>
            } 
          />

          {/* NOVA Rota para o formulário de CRIAÇÃO de Cliente - PROTEGIDA */}
          <Route 
            path="/clientes/novo" // URL para cadastrar novo cliente
            element={
              <PrivateRoute>
                <ClienteForm />
              </PrivateRoute>
            } 
          />

          {/* NOVA Rota para o formulário de EDIÇÃO de Cliente - PROTEGIDA */}
          {/* O ':id' é um parâmetro de URL que ClienteForm usará para carregar o cliente */}
          <Route 
            path="/clientes/editar/:id" 
            element={
              <PrivateRoute>
                <ClienteForm />
              </PrivateRoute>
            } 
          />

        </Routes>
      </div>
    </Router>
  );
}

export default App;