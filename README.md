# Este projeto foi feito utilizando Python 3.10.11

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

   - No Windows, exemplo de comandos:
      ```bash
     python -m venv .venv
      .venv\Scripts\activate
      ```

   - No Linux/macOS, exemplo de comandos:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

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
