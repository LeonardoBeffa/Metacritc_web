# Coletor de Dados de Jogos do Metacritic

Este script coleta informações sobre jogos de PC listados no Metacritic e armazena os dados em um arquivo CSV. Ele realiza scraping das páginas de jogos e extrai detalhes como nome, ano de lançamento e nota média dos jogos.

## Funcionalidades

- **Coleta de Dados**: Acessa o site Metacritic e coleta informações sobre jogos de PC, navegando por múltiplas páginas de resultados.
- **Extração de Dados**:
  - **Nome do Jogo**: Extraído do título do jogo listado na página.
  - **Ano de Lançamento**: Extraído da seção de metadados do jogo.
  - **Nota Média**: Capturada da seção de avaliação do jogo.
- **Armazenamento de Dados**: Os dados são salvos em um arquivo CSV chamado `Games_metacritc.csv`, localizado no diretório especificado pela variável `destino`.

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:

- `requests`
- `beautifulsoup4`
- `pandas`

Você pode instalar as bibliotecas necessárias usando pip:

```bash
pip install requests beautifulsoup4 pandas
