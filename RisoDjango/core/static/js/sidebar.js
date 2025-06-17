document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('toggleSidebar');
  const labels = document.querySelectorAll('.sidebar-label');
  const title = document.getElementById('sidebar-title');
  const closebtn = document.getElementById('close-btn');
  const openbtn = document.getElementById('open-btn');

  const setCollapsed = (collapsed) => {
    const isCollapsed = collapsed === 'true';

    //salva em cookie o stado da sidebar
    document.cookie = `sidebar_collapsed=${collapsed}; path=/; max-age=31536000`;

    // aplica largura
    sidebar.style.width = isCollapsed ? '5.5rem' : '16rem';

    labels.forEach(label => {
      label.classList.toggle('hidden', isCollapsed);
    });

    if (title) {
      title.classList.toggle('hidden', isCollapsed);
    }
    
    //funcionalidade do botao para abrir e fechar sidebar
    if (isCollapsed) {
      closebtn.classList.toggle('hidden', true);
      openbtn.classList.toggle('hidden', false);
    } else {
      closebtn.classList.toggle('hidden', false);
      openbtn.classList.toggle('hidden', true);
    }

    sidebar.dataset.collapsed = collapsed;
  };

  // Pega o estado salvo no cookie
  const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts.pop().split(';').shift() : null;
  };

  const initial = getCookie('sidebar_collapsed') || 'false';
  setCollapsed(initial);

  toggleBtn?.addEventListener('click', () => {
    const isCollapsed = sidebar.dataset.collapsed === 'true';
    setCollapsed(!isCollapsed + '');
  });
});
