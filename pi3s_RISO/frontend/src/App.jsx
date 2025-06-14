// src/App.jsx
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Home from './components/Home';
import PrivateRoute from './components/PrivateRoute'; // <-- Importe o PrivateRoute

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Rota para a página de Login - esta deve ser sempre pública */}
          <Route path="/login" element={<Login />} />

          {/* Rota para a Página Inicial (Home) - PROTEGIDA agora */}
          {/* Envolvemos o componente Home com o PrivateRoute */}
          <Route 
            path="/" 
            element={
              <PrivateRoute> {/* <-- Use o PrivateRoute aqui */}
                <Home />
              </PrivateRoute>
            } 
          /> 
        </Routes>
      </div>
    </Router>
  );
}

export default App;