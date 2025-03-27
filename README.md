# Intuitive Care

 Este projeto foi feito utilizando Python 3.10.11 e postgres 13.4

## 1 - Web Scrapping

Este módulo realiza o web scrapping para acessar a página de atualização do rol de procedimentos da ANS, extrair os links dos PDFs dos anexos, baixar os arquivos e compactá-los em um único arquivo ZIP.

### Como Rodar

1. Navegue até a pasta do projeto:
   ```bash
   cd web_scraping
    ```

2. Crie e Ative um Ambiente Virtual:
   Recomenda-se criar um ambiente virtual para isolar as dependências do projeto. Consulte a documentação do venv em:
   https://docs.python.org/3/library/venv.html

3. Instale as Dependências:
   Certifique-se de que o arquivo requirements.txt está atualizado e instale as dependências:
   ```bash
    pip install -r requirements.txt
    ```
4. Execute o Script Principal:
   Após instalar as dependências, execute o arquivo main.py:
   ```bash
    python main.py
    ```
### Alterando o Driver

Por padrão, o driver está configurado para utilizar o Chrome. Se desejar usar outro navegador, edite o arquivo driver_config.py.


## 2 - Tranformação de dados
Este módulo extrai os dados do PDF do Anexo I baixado na parte 1, salva em formato .csv, compacta em um arquivo chamado Teste_lucas_petruci.zip, e substitui OD e AMB por sua descrição completa


### Como Rodar
   1. Rode a parte 1 para ter os arquivos em .pdf
      
   2. Navegue até a pasta do projeto:
   ```bash
   cd data_transformation
   ```
   3. Execute o Script Principal:
   ```bash
   python main.py
   ```

## 3 - Banco de dados
Neste módulo, temos os scripts .sql que criam as tabelas, inserem dados no banco de dados PostgreSQL e realizam as Query. Utilizei o PostgreSQL 13.4 em conjunto com o Docker para facilitar o processo de instalação e execução.

### Como Configurar o Banco de dados (pode ser feito de outras formas)
  1. Criar e Rodar o conteiner docker
  
   ```bash
   docker run --name postgres-container -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres:13.4
   ```
  2. Utilize os valores usados para criar o container para conectar ao SQLTools
    
  3. Criar Database
  ```bash
  CREATE DATABASE intuitive_care_db
  ```
 4. Para conectar-se ao banco de dados utilizando o SQLTools no VSCode, utilize as seguintes credenciais do conteiner
    
 5. Acesse a pasta data_base/sql, primeiro rode o create_table.sql, depois o insert_data.sql(caso necessario mude o path) e depois o queries.sql
 
