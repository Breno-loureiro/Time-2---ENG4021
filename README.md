# ⚽ CAMISA 12

> **O torcedor também tem seu lugar em campo.**

O **CAMISA 12** é um marketplace de artigos esportivos com foco em **camisas de futebol, NBA e NFL** — atuais, retrô e de colecionador. O nome vem da ideia de que o torcedor é o **"12º jogador"** do time.

A plataforma reúne em um só lugar produtos de várias lojas e vendedores, para que o usuário possa **pesquisar, comparar preços e consultar avaliações** antes de comprar.

Projeto acadêmico desenvolvido em grupo na disciplina **ENG4021** da **PUC-Rio** (2026.2).

---

## 📌 Sumário

- [O problema](#-o-problema)
- [Público-alvo](#-público-alvo)
- [Diferenciais](#-diferenciais)
- [Funcionalidades](#-funcionalidades)
- [O que já está pronto](#-o-que-já-está-pronto)
- [Protótipos no Figma](#-protótipos-no-figma)
- [Tecnologias](#-tecnologias)
- [Estrutura do repositório](#-estrutura-do-repositório)
- [Como rodar o projeto Django](#-como-rodar-o-projeto-django)
- [Identidade visual](#-identidade-visual)
- [Documentação](#-documentação)
- [Equipe](#-equipe)

---

## ❓ O problema

Hoje, quem quer comprar uma camisa de time precisa pesquisar em várias lojas, perfis de Instagram e grupos de WhatsApp. Isso gera três dificuldades:

1. **Informação espalhada:** o mesmo produto aparece em vários lugares, com preços diferentes.
2. **Falta de confiança:** é difícil saber se o vendedor é confiável e se o produto é original ou está em bom estado.
3. **Pouca visibilidade para pequenos vendedores:** revendedores e lojas pequenas não têm um marketplace próprio para alcançar mais compradores.

O CAMISA 12 resolve isso centralizando os anúncios, organizando por esporte, liga e time, e mostrando avaliações de produtos e de vendedores.

---

## 👥 Público-alvo

**Compradores**
- Torcedores que procuram a camisa do seu time, de um jogador ou de uma temporada específica.
- Colecionadores e caçadores de camisas raras, antigas e retrô.
- Quem quer comparar o preço do mesmo produto em lojas diferentes.
- Quem já compra pelo Instagram ou WhatsApp, mas quer verificar a reputação do vendedor antes.
- Praticantes de esportes e fãs de artigos esportivos (chuteiras, bonés, jaquetas, acessórios).

**Vendedores**
- Revendedores independentes e lojas de Instagram que querem alcançar mais clientes.
- Pequenas lojas esportivas que querem divulgar seu catálogo.
- Vendedores especializados em camisas retrô, importadas ou de clubes específicos.

A lista completa está em [`Documentos/Público-Alvo`](Documentos/Público-Alvo).

---

## ⭐ Diferenciais

- **Comparação entre vendedores:** o mesmo produto, ou produtos parecidos, lado a lado em lojas diferentes.
- **Especialização em artigos esportivos:** busca organizada por esporte, liga, time, temporada, modelo e tipo de produto.
- **Avaliação de produtos e de vendedores:** o usuário vê a nota do produto e a reputação de quem vende.
- **Nota de conservação da camisa:** cada camisa usada recebe uma nota de 1 a 5 estrelas a partir de critérios objetivos (tecido, manchas, escudo, estampas, nome e número, furos e desbotamento). Os critérios estão em [`Documentos/Sistema Avaliação Camisa`](Documentos/Sistema%20Avaliação%20Camisa).
- **Mais transparência:** avaliações, dados do vendedor e comparação ajudam o usuário a comprar com segurança.

---

## 🧩 Funcionalidades

Requisitos funcionais previstos para o sistema (documento completo em [`Documentos/RF_RNF_Camisa_12.pdf`](Documentos/RF_RNF_Camisa_12.pdf)):

| ID | Requisito | Descrição resumida |
|----|-----------|--------------------|
| RF01 | Cadastro de usuário | Criar conta com nome, e-mail e senha. |
| RF02 | Autenticação | Fazer login e logout. |
| RF03 | Pesquisa de produtos | Buscar por nome, categoria, marca, time, ano e modelo. |
| RF04 | Filtros e ordenação | Filtrar e ordenar por preço, avaliação, marca e ano. |
| RF05 | Detalhes do produto | Ver imagens, descrição, marca, modelo, ano, preço e avaliações. |
| RF06 | Consulta de lojas | Ver quais lojas vendem determinado produto. |
| RF07 | Comparação de preços | Comparar o mesmo produto em lojas diferentes. |
| RF08 | Avaliação de produtos | Dar nota e comentário para um produto. |
| RF09 | Avaliação de lojas | Dar nota e comentário para uma loja ou vendedor. |
| RF10 | Cálculo de média | Calcular a nota média de produtos e lojas. |
| RF11 | Acesso à loja | Ser direcionado ao site da loja para comprar. |
| RF12 | Favoritos | Salvar produtos favoritos. |
| RF13 | Denúncias | Denunciar anúncios ou vendedores suspeitos. |
| RF14 | Gestão administrativa | Administrar usuários, produtos e lojas. |
| RF15 | Moderação | Moderar avaliações e anúncios. |

Os requisitos não funcionais (RNF01 a RNF10) tratam de usabilidade e responsividade, desempenho, segurança de senhas, privacidade, controle de acesso, integridade dos dados, disponibilidade, manutenibilidade, compatibilidade e validação de entradas.

---

## ✅ O que já está pronto

### Telas do site (HTML + CSS + JavaScript)

Pasta [`Telas html`](Telas%20html):

| Tela | Arquivo | Ver no navegador |
|------|---------|------------------|
| Camisas de futebol (com busca, filtros e favoritos) | [`futebol.html`](Telas%20html/futebol.html) | [abrir](https://htmlpreview.github.io/?https://github.com/RicardoMartiinns/Time-2---ENG4021/blob/main/Telas%20html/futebol.html) |
| Produtos NBA | [`nba.html`](Telas%20html/nba.html) | [abrir](https://htmlpreview.github.io/?https://github.com/RicardoMartiinns/Time-2---ENG4021/blob/main/Telas%20html/nba.html) |
| Produtos NFL | [`nfl.html`](Telas%20html/nfl.html) | [abrir](https://htmlpreview.github.io/?https://github.com/RicardoMartiinns/Time-2---ENG4021/blob/main/Telas%20html/nfl.html) |
| Lojas parceiras | [`lojas.html`](Telas%20html/lojas.html) | [abrir](https://htmlpreview.github.io/?https://github.com/RicardoMartiinns/Time-2---ENG4021/blob/main/Telas%20html/lojas.html) |
| Lançamento (lista de espera) | [`lancamento.html`](Telas%20html/lancamento.html) | [abrir](https://htmlpreview.github.io/?https://github.com/RicardoMartiinns/Time-2---ENG4021/blob/main/Telas%20html/lancamento.html) |
| Sobre | [`sobre.html`](Telas%20html/sobre.html) | [abrir](https://htmlpreview.github.io/?https://github.com/RicardoMartiinns/Time-2---ENG4021/blob/main/Telas%20html/sobre.html) |

Pasta [`HTML`](HTML), com telas de usuário e a tela desenhada no Figma:

| Tela | Arquivo |
|------|---------|
| Login de usuário | [`HTML/LOGIN USUARIO`](HTML/LOGIN%20USUARIO) |
| Remoção de usuário | [`HTML/REMOCAO USUARIO`](HTML/REMOCAO%20USUARIO) |
| Listagem de usuários | [`HTML/LISTAR USUARIOS`](HTML/LISTAR%20USUARIOS) |
| Camisas de futebol (versão do Figma) | [`HTML/Tela Figma`](HTML/Tela%20Figma) |

### Back-end em Django

Pasta [`Django`](Django), com o projeto `Camisa12` e os bancos de dados da página de futebol:

- **Tamanhos de camisa:** P, M, G e GG, com largura e altura em cm.
- **Notas de conservação:** escala de 1 a 5, exibida na página `/notas/`.
- **Times:** nome, sigla e liga.
- **Ligas:** nome, país e divisão.
- **Confederações:** sigla e continente.

Todos os bancos podem ser cadastrados e editados pela interface administrativa (`/admin/`).

### Modelagem de dados

- Diagrama de classes (usuário, cliente, vendedor, produto, categoria, carrinho, pedido, pagamento e avaliação) em [`Escopo/ModelagemDeDados.md`](Escopo/ModelagemDeDados.md).
- Script SQL do banco em [`Documentos/Base de dados`](Documentos/Base%20de%20dados).
- Estrutura padrão de um anúncio em JSON em [`Documentos/Estrutura de dados do anúncio em JSON.md`](Documentos/Estrutura%20de%20dados%20do%20anúncio%20em%20JSON.md).

---

## 🎨 Protótipos no Figma

- [Site funcional no Figma Make](https://www.figma.com/make/iLrotWCERcVh2ebW9PvYsO/Site-Camisa-12?code-node-id=0-6&p=f&t=vcp3FbC8cJlgoqY1-0&fullscreen=1)
- [Protótipo: Camisas de Futebol](https://www.figma.com/proto/CG8wKh9Z6EisBmtXkcrFM9/P%C3%A1ginas-do-site?node-id=26-1286&p=f&t=Ad7ZKcxg5aPrd2cU-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1)
- [Protótipo: NBA](https://www.figma.com/proto/CG8wKh9Z6EisBmtXkcrFM9/P%C3%A1ginas-do-site?node-id=36-1637&p=f&t=Ad7ZKcxg5aPrd2cU-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1)
- [Protótipo: NFL](https://www.figma.com/proto/CG8wKh9Z6EisBmtXkcrFM9/P%C3%A1ginas-do-site?node-id=37-1306&p=f&t=VSv4KuYbYLFxAYwh-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1)

Para ver a versão de celular no Figma Make, troque a pré-visualização para celular nas opções de visualização.

---

## 🛠 Tecnologias

| Parte | Tecnologia |
|-------|------------|
| Protótipos e design | Figma e Figma Make |
| Front-end | HTML5, CSS3 (com media queries para celular e tablet) e JavaScript |
| Back-end | Python + Django |
| Banco de dados | SQLite (Django) e script SQL da modelagem |
| Versionamento | Git, GitHub e GitHub Codespaces |
| Organização | Kanban por sprint |

---

## 📁 Estrutura do repositório

```
Time-2---ENG4021/
├── Django/                 → projeto Django (back-end e bancos de dados)
├── Documentos/             → requisitos, concorrência, público-alvo, monetização, riscos, fluxogramas
├── Entrevista Forms/       → roteiro e resultados das entrevistas e formulários
├── Escopo/                 → definição do escopo e modelagem de dados
├── Figma/                  → links dos protótipos
├── HTML/                   → telas de usuário e tela do Figma em HTML/CSS
├── IdeiasSite/             → ideias de funcionalidades e clube de membros
├── Identidade visual/      → cores, fontes, logotipo e testes
├── Requisitos e Processos/ → requisitos funcionais e fluxo de compra
├── Slogan/                 → slogan do projeto
├── Telas html/             → telas do site (futebol, NBA, NFL, lojas, lançamento, sobre)
└── README.md               → este arquivo
```

---

## ▶ Como rodar o projeto Django

No terminal do Codespace, a partir da raiz do repositório:

```bash
cd Django
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Depois:

1. Na aba **Ports**, deixe a porta **8000** como **Public** e abra o link.
2. Acrescente **`/admin/`** no final do endereço e entre com o superusuário para cadastrar tamanhos, notas, times, ligas e confederações.
3. Acrescente **`/notas/`** no final do endereço para ver a escala de notas de conservação.

---

## 🖌 Identidade visual

A ideia visual é fazer o usuário se sentir **dentro de um estádio em dia de clássico**.

- **Preto:** fundo, simulando a noite.
- **Branco:** caixas de conteúdo, simulando os holofotes.
- **Verde:** destaque, simulando o gramado.
- **Laranja:** segunda cor de destaque.

Páginas de um time ou liga usam também as cores dessa entidade. Detalhes em [`Identidade visual`](Identidade%20visual).

---

## 📚 Documentação

| Documento | Onde está |
|-----------|-----------|
| Requisitos funcionais e não funcionais | [`Documentos/RF_RNF_Camisa_12.pdf`](Documentos/RF_RNF_Camisa_12.pdf) |
| Análise de concorrência | [`Documentos/Concorrentes`](Documentos/Concorrentes) |
| Público-alvo | [`Documentos/Público-Alvo`](Documentos/Público-Alvo) |
| Sistema de avaliação da camisa | [`Documentos/Sistema Avaliação Camisa`](Documentos/Sistema%20Avaliação%20Camisa) |
| Monetização | [`Documentos/Monetizacao.pdf`](Documentos/Monetizacao.pdf) |
| Matriz de risco | [`Documentos/Matriz de risco - Página1.pdf`](Documentos/Matriz%20de%20risco%20-%20Página1.pdf) |
| Impactos positivos e negativos | [`Documentos/Análise dos impactos positivos e negativos do Camisa12.pdf`](Documentos/Análise%20dos%20impactos%20positivos%20e%20negativos%20do%20Camisa12.pdf) |
| Fluxogramas do usuário e do vendedor | [`Documentos/FLUXOGRAMA`](Documentos/FLUXOGRAMA) |
| Entrevistas e formulários | [`Entrevista Forms`](Entrevista%20Forms) |
| Escopo e modelagem de dados | [`Escopo`](Escopo) |
| Clube de membros | [`IdeiasSite/Definição de benefícios para o clube de membros.txt`](IdeiasSite/Definição%20de%20benefícios%20para%20o%20clube%20de%20membros.txt) |

---

## 🤝 Equipe

| Integrante | GitHub |
|------------|--------|
| Breno Loureiro | [@Breno-loureiro](https://github.com/Breno-loureiro) |
| Carlos Duval | [@cczld](https://github.com/cczld) |
| Pedro Kalache Costa | [@PedroKalache](https://github.com/PedroKalache) |
| Pedro Pagliuso Saceanu | [@pedrosaceanu](https://github.com/pedrosaceanu) |
| Rafael K. Amaral | [@RafaelKAmaral](https://github.com/RafaelKAmaral) |
| Ricardo Martins | [@RicardoMartiinns](https://github.com/RicardoMartiinns) |

---

<p align="center"><b>CAMISA 12</b> — O torcedor também tem seu lugar em campo. ⚽</p>
