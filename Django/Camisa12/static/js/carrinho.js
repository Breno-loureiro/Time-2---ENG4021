(() => {
  const CHAVE_CARRINHO = 'camisa12-carrinho-v1';
  const formatadorMoeda = new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL'
  });

  const lerCarrinho = () => {
    try {
      const dados = JSON.parse(localStorage.getItem(CHAVE_CARRINHO) || '[]');
      return Array.isArray(dados) ? dados : [];
    } catch {
      return [];
    }
  };

  const salvarCarrinho = (itens) => {
    try {
      localStorage.setItem(CHAVE_CARRINHO, JSON.stringify(itens));
      atualizarIndicadores();
      return true;
    } catch (erro) {
      console.error('Não foi possível salvar o carrinho neste navegador.', erro);
      alert('Não foi possível salvar o carrinho. Verifique as configurações de armazenamento do navegador.');
      return false;
    }
  };

  const quantidadeTotal = (itens) => itens.reduce((soma, item) => soma + item.quantidade, 0);

  function atualizarIndicadores() {
    const quantidade = quantidadeTotal(lerCarrinho());
    document.querySelectorAll('.carrinho__qtd').forEach(indicador => {
      indicador.textContent = String(quantidade);
      indicador.setAttribute('aria-label', `${quantidade} ${quantidade === 1 ? 'item' : 'itens'} no carrinho`);
    });
  }

  const normalizar = (texto) => texto
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim();

  function adicionarProduto(card, botao) {
    const nome = card.querySelector('.card__nome')?.textContent.trim();
    const time = card.querySelector('.card__time')?.textContent.trim() || '';
    const textoPreco = card.querySelector('.card__preco')?.textContent || '';
    const preco = Number(textoPreco.replace(/[^\d,]/g, '').replace(',', '.'));
    const categoria = document.body.dataset.categoria || 'Esportes';

    if (!nome || !Number.isFinite(preco) || preco <= 0) {
      alert('Não foi possível adicionar este produto. Confira o nome e o preço no catálogo.');
      return;
    }

    const id = normalizar(`${categoria}-${time}-${nome}`);
    const itens = lerCarrinho();
    const existente = itens.find(item => item.id === id);

    if (existente) {
      existente.quantidade += 1;
    } else {
      itens.push({ id, nome, time, categoria, preco, quantidade: 1 });
    }

    if (salvarCarrinho(itens)) {
      const textoOriginal = botao.textContent;
      botao.textContent = 'Adicionado ✓';
      botao.classList.add('adicionado');
      botao.disabled = true;
      window.setTimeout(() => {
        botao.textContent = textoOriginal;
        botao.classList.remove('adicionado');
        botao.disabled = false;
      }, 1100);
    }
  }

  // Integra os botões de todos os produtos das páginas de catálogo.
  document.querySelectorAll('.card').forEach(card => {
    const botao = card.querySelector('.btn--adicionar-carrinho');
    if (!botao) return;
    botao.addEventListener('click', () => adicionarProduto(card, botao));
  });

  const lista = document.querySelector('#carrinho-itens');
  if (lista) {
    const vazio = document.querySelector('#carrinho-vazio');
    const conteudo = document.querySelector('#carrinho-conteudo');
    const subtotalEl = document.querySelector('#carrinho-subtotal');
    const quantidadeEl = document.querySelector('#carrinho-total-itens');
    const botaoEsvaziar = document.querySelector('#carrinho-esvaziar');
    const botaoFinalizar = document.querySelector('#finalizar-pedido');

    const criarBotao = (texto, acao, id, rotulo, desabilitado = false) => {
      const botao = document.createElement('button');
      botao.type = 'button';
      botao.className = 'controle-quantidade__botao';
      botao.textContent = texto;
      botao.dataset.action = acao;
      botao.dataset.id = id;
      botao.setAttribute('aria-label', rotulo);
      botao.disabled = desabilitado;
      return botao;
    };

    function renderizarCarrinho() {
      const itens = lerCarrinho();
      const temItens = itens.length > 0;
      lista.replaceChildren();
      vazio.hidden = temItens;
      conteudo.hidden = !temItens;

      itens.forEach(item => {
        const linha = document.createElement('article');
        linha.className = 'item-carrinho';

        const miniatura = document.createElement('div');
        miniatura.className = 'item-carrinho__miniatura';
        miniatura.setAttribute('aria-hidden', 'true');
        miniatura.textContent = '12';

        const informacoes = document.createElement('div');
        informacoes.className = 'item-carrinho__informacoes';

        const categoria = document.createElement('span');
        categoria.className = 'item-carrinho__categoria';
        categoria.textContent = `${item.categoria} · ${item.time}`;

        const nome = document.createElement('h3');
        nome.className = 'item-carrinho__nome';
        nome.textContent = item.nome;

        const precoUnitario = document.createElement('p');
        precoUnitario.className = 'item-carrinho__preco-unitario';
        precoUnitario.textContent = `${formatadorMoeda.format(item.preco)} por unidade`;

        informacoes.append(categoria, nome, precoUnitario);

        const quantidade = document.createElement('div');
        quantidade.className = 'controle-quantidade';
        quantidade.append(
          criarBotao('−', 'diminuir', item.id, `Diminuir quantidade de ${item.nome}`, item.quantidade <= 1)
        );

        const valorQuantidade = document.createElement('span');
        valorQuantidade.className = 'controle-quantidade__valor';
        valorQuantidade.textContent = String(item.quantidade);
        valorQuantidade.setAttribute('aria-label', `Quantidade: ${item.quantidade}`);

        quantidade.append(
          valorQuantidade,
          criarBotao('+', 'aumentar', item.id, `Aumentar quantidade de ${item.nome}`)
        );

        const ladoDireito = document.createElement('div');
        ladoDireito.className = 'item-carrinho__lado-direito';

        const totalItem = document.createElement('strong');
        totalItem.className = 'item-carrinho__total';
        totalItem.textContent = formatadorMoeda.format(item.preco * item.quantidade);

        const remover = document.createElement('button');
        remover.type = 'button';
        remover.className = 'item-carrinho__remover';
        remover.dataset.action = 'remover';
        remover.dataset.id = item.id;
        remover.textContent = 'Remover';

        ladoDireito.append(totalItem, remover);
        linha.append(miniatura, informacoes, quantidade, ladoDireito);
        lista.appendChild(linha);
      });

      const subtotal = itens.reduce((soma, item) => soma + item.preco * item.quantidade, 0);
      subtotalEl.textContent = formatadorMoeda.format(subtotal);
      quantidadeEl.textContent = String(quantidadeTotal(itens));
      atualizarIndicadores();
    }

    lista.addEventListener('click', event => {
      const botao = event.target.closest('button[data-action]');
      if (!botao) return;

      const { action, id } = botao.dataset;
      let itens = lerCarrinho();
      const item = itens.find(produto => produto.id === id);
      if (!item) return;

      if (action === 'aumentar') item.quantidade += 1;
      if (action === 'diminuir' && item.quantidade > 1) item.quantidade -= 1;
      if (action === 'remover') itens = itens.filter(produto => produto.id !== id);

      if (salvarCarrinho(itens)) renderizarCarrinho();
    });

    botaoEsvaziar?.addEventListener('click', () => {
      if (salvarCarrinho([])) renderizarCarrinho();
    });

    botaoFinalizar?.addEventListener('click', () => {
      alert('Este é um protótipo acadêmico. A integração com pagamento e finalização real do pedido ainda não está configurada.');
    });

    renderizarCarrinho();
  }

  atualizarIndicadores();
})();
