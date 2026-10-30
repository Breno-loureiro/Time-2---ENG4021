(() => {
  const catalogo = document.querySelector('.produtos');
  const filtros = document.querySelector('.filtros');
  if (!catalogo || !filtros) return;

  const cards = [...catalogo.querySelectorAll('.card')];
  const busca = filtros.querySelector('input[type="search"]');
  const filtroTime = filtros.querySelector('.filtro-time');
  const filtroPreco = filtros.querySelector('select[aria-label="Faixa de preço"]');
  const ordenar = filtros.querySelector('select[aria-label="Ordenar"]');
  const filtroFavoritos = filtros.querySelector('.filtro-favoritos');
  const total = document.querySelector('.catalogo__total');
  const chaveFavoritos = 'camisa12-favoritos-v1';

  const lerFavoritos = () => {
    try { return JSON.parse(localStorage.getItem(chaveFavoritos) || '[]'); }
    catch { return []; }
  };
  const salvarFavoritos = (ids) => localStorage.setItem(chaveFavoritos, JSON.stringify(ids));
  const normalizar = (texto) => texto.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
  const precoDo = (card) => {
    const texto = card.querySelector('.card__preco')?.textContent || '';
    return Number(texto.replace(/[^\d,]/g, '').replace('.', '').replace(',', '.')) || 0;
  };
  const idDo = (card) => {
    const nome = card.querySelector('.card__nome')?.textContent || '';
    const time = card.querySelector('.card__time')?.textContent || '';
    return normalizar(`${time}-${nome}`);
  };

  // Preenche o filtro de times com os times realmente presentes nesta página.
  if (filtroTime) {
    const times = [...new Set(cards.map(c => c.querySelector('.card__time')?.textContent.trim()).filter(Boolean))].sort();
    times.forEach(time => {
      const option = document.createElement('option');
      option.value = time;
      option.textContent = time;
      filtroTime.appendChild(option);
    });
  }

  cards.forEach(card => {
    const midia = card.querySelector('.card__midia');
    if (midia && !midia.querySelector('.favorito-btn')) {
      const botao = document.createElement('button');
      botao.type = 'button';
      botao.className = 'favorito-btn';
      botao.setAttribute('aria-label', 'Adicionar aos favoritos');
      botao.innerHTML = '♡ <span>Favoritar</span>';
      midia.appendChild(botao);
      botao.addEventListener('click', () => {
        const favoritos = lerFavoritos();
        const id = idDo(card);
        const atualizado = favoritos.includes(id) ? favoritos.filter(x => x !== id) : [...favoritos, id];
        salvarFavoritos(atualizado);
        atualizarBotoesFavoritos();
        aplicarFiltros();
      });
    }
  });

  function atualizarBotoesFavoritos() {
    const favoritos = lerFavoritos();
    cards.forEach(card => {
      const botao = card.querySelector('.favorito-btn');
      if (!botao) return;
      const ativo = favoritos.includes(idDo(card));
      botao.classList.toggle('favorito-btn--ativo', ativo);
      botao.innerHTML = ativo ? '♥ <span>Favoritado</span>' : '♡ <span>Favoritar</span>';
      botao.setAttribute('aria-pressed', String(ativo));
      botao.setAttribute('aria-label', ativo ? 'Remover dos favoritos' : 'Adicionar aos favoritos');
    });
  }

  function aplicarFiltros() {
    const termo = normalizar(busca?.value || '');
    const timeSelecionado = filtroTime?.value || '';
    const faixa = filtroPreco?.selectedIndex ?? 0;
    const soFavoritos = filtroFavoritos?.value === 'favoritos';
    const favoritos = lerFavoritos();

    let visiveis = cards.filter(card => {
      const texto = normalizar(card.textContent);
      const preco = precoDo(card);
      const bateBusca = !termo || texto.includes(termo);
      const bateTime = !timeSelecionado || card.querySelector('.card__time')?.textContent.trim() === timeSelecionado;
      const batePreco = faixa === 0 || (faixa === 1 && preco <= 200) ||
        (faixa === 2 && preco > 200 && preco <= 350) || (faixa === 3 && preco > 350);
      const bateFavoritos = !soFavoritos || favoritos.includes(idDo(card));
      return bateBusca && bateTime && batePreco && bateFavoritos;
    });

    const modoOrdenacao = ordenar?.selectedIndex ?? 0;
    if (modoOrdenacao === 1) visiveis.sort((a,b) => precoDo(a)-precoDo(b));
    if (modoOrdenacao === 2) visiveis.sort((a,b) => precoDo(b)-precoDo(a));
    if (modoOrdenacao === 3) {
      const nota = card => Number(card.querySelector('.avaliacao')?.textContent.match(/[\d.]+/)?.[0] || 0);
      visiveis.sort((a,b) => nota(b)-nota(a));
    }

    cards.forEach(card => { card.hidden = !visiveis.includes(card); });
    if (total) total.textContent = `${visiveis.length} produto${visiveis.length === 1 ? '' : 's'} encontrado${visiveis.length === 1 ? '' : 's'}`;
  }

  filtros.addEventListener('submit', event => event.preventDefault());
  [busca, filtroTime, filtroPreco, ordenar, filtroFavoritos]
    .filter(Boolean).forEach(campo => campo.addEventListener(campo === busca ? 'input' : 'change', aplicarFiltros));

  atualizarBotoesFavoritos();
  aplicarFiltros();
})();