# Restaurant POS

[![Build Status](https://travis-ci.org/seu-username/restaurant_point_of_sales.svg?branch=master)](https://travis-ci.org/seu-username/restaurant_point_of_sales)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/downloads/)

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/pedro3mDev/engenharia_software
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd engenharia_software/restaurant_point_of_sales
    ```

3. Crie um ambiente virtual (recomendado):
    ```bash
    python3 -m venv venv
    ```

4. Ative o ambiente virtual:
    - No Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
    - No Windows (PowerShell):
        ```bash
        .\venv\Scripts\Activate
        ```

5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

6. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

8. Acesse o projeto em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

