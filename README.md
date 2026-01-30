Scrap Folha SP — News Scraper

Projeto desenvolvido em Python para coleta automatizada de notícias do portal Folha de S.Paulo utilizando Selenium WebDriver. A aplicação permite que o usuário informe um tema de interesse via terminal, realiza a busca dinâmica no site e extrai informações estruturadas das notícias na primeira página do site, exportando os resultados para um arquivo CSV.

O objetivo do projeto é demonstrar competências em automação web, scraping, organização de código e separação de responsabilidades, simulando um cenário real de coleta e tratamento de dados para uso profissional.

Funcionalidades
- Entrada interativa de tema de busca via terminal
- Geração dinâmica da URL de busca
- Scraping da página de resultados da Folha de S.Paulo
- Extração de título, descrição, data de publicação, URL da notícia e URL da imagem
- Exportação dos dados para arquivo CSV

Tecnologias Utilizadas
- Python 3.11+
- Selenium
- Google Chrome
- Poetry para gerenciamento de dependências e ambiente virtual

Estrutura do Projeto
src/
- main.py
- orchestrator/orchestrator.py
- services/driver.py
- services/folha_search.py
- services/search_query.py
- services/excel.py

Arquitetura
O projeto foi estruturado de forma simples e clara, com responsabilidades bem definidas. O arquivo main.py atua apenas como ponto de entrada da aplicação. O orchestrator centraliza o fluxo de execução, com tratativa para erros, controlando o ciclo de vida do Selenium WebDriver e coordenando os serviços. A camada services concentra a lógica específica de cada responsabilidade, como criação do driver, scraping, entrada de dados do usuário e persistência em CSV.

Instalação
1. Clonar o repositório
git clone <url-do-repositorio>
cd Scrap-Folha-SP

2. Instalar o Poetry
pip install poetry

3. Instalar as dependências
poetry install

Execução
poetry run python src/main.py

Após iniciar, o sistema solicitará a entrada do tema de busca pelo terminal. O usuário digita o assunto desejado e o scraping é executado automaticamente.

Saída
O programa gera um arquivo noticias.csv contendo os dados coletados. As colunas do arquivo são: title, description, date, url e image_url. O CSV pode ser utilizado posteriormente para análise, importação em sistemas ou armazenamento em banco de dados.

Requisitos
- Google Chrome instalado
- Acesso à internet
- Terminal com suporte a entrada interativa

O Selenium Manager é utilizado para resolução automática do driver do navegador.

Considerações Técnicas
O scraping depende da estrutura atual do site da Folha de S.Paulo. Alterações no HTML podem exigir ajustes nos seletores utilizados. O projeto foi desenvolvido com foco educacional e demonstrativo, seguindo boas práticas de organização e clareza de código.

Possíveis Evoluções
- Implementação de paginação automática
- Persistência em banco de dados
- Exportação alternativa em JSON
- Execução configurável em modo headless
- Suporte a múltiplas fontes de notícias


