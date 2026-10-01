Este documento define a estrutura padrão de dados de um anúncio do CAMISA 12, servindo de referência para a implementação do front-end, do back-end e do banco de dados, e garantindo que anúncios de futebol, NBA e NFL sejam tratados de forma consistente em todo o sistema.

````json
{
  "id": "anc_10482",
  "vendedor_id": "usr_2291",
  "status": "publicado",
  "data_criacao": "2026-10-01T17:20:00-03:00",
  "titulo": "Jersey Chicago Bulls 1997-98 - Michael Jordan #23",
  "descricao": "Jersey original da temporada 97-98, pouco uso, sem furos ou manchas.",
  "esporte": "basquete",
  "liga": "NBA",
  "time": "Chicago Bulls",
  "temporada": "1997-98",
  "tipo_produto": "camisa",
  "modelo": "titular",
  "fornecedor": "Champion",
  "jogador": {
    "nome": "Michael Jordan",
    "numero": 23
  },
  "tamanho": "G",
  "estado_conservacao": "otimo",
  "autenticidade": {
    "categoria": "original_de_epoca",
    "codigo_produto": null,
    "selo_verificado": false
  },
  "preco": 1890.00,
  "moeda": "BRL",
  "frete": {
    "peso_g": 300,
    "altura_cm": 4,
    "largura_cm": 25,
    "comprimento_cm": 35,
    "cep_origem": "22451900"
  },
  "fotos": [
    { "tipo": "frente", "url": "https://res.cloudinary.com/camisa12/frente_10482.jpg" },
    { "tipo": "costas", "url": "https://res.cloudinary.com/camisa12/costas_10482.jpg" },
    { "tipo": "etiqueta", "url": "https://res.cloudinary.com/camisa12/etiqueta_10482.jpg" }
  ]
}
````
Decisôes de projeto
-Um formato para todos os esportes:em vez de campos como "clube" (futebol) e "franquia" (NBA e NFL), usa-se `time` e `liga`, que servem para todos.
-Valores fixos onde possível: campos como `estado_conservacao` e `autenticidade.categoria` aceitam só opções predefinidas, o que mantém os filtros consistentes.
-Campos opcionais `jogador` e `codigo_produto` podem ser `null`, porque muitas camisas não têm nome nem número, e camisas antigas muitas vezes não têm código.
-Fotos com tipo:classificar cada foto permite ao sistema verificar se o anúncio tem as fotos obrigatórias antes de publicá-lo.