# Sistema de Controle em Nuvem com Python e Socket

Este projeto implementa um sistema de controle em nuvem usando **Python** e **Socket** para comunicação entre o servidor e o cliente. O servidor é responsável por executar a planta (ou processo) que precisa ser controlado, enquanto o cliente é responsável pelo controle e monitoramento.

![Dashboard](https://github.com/hewertonfl/PROJETO_SOCKET_AWS/blob/master/assets/dashboard.png)
## Funcionalidades

-   **Servidor**:

    -   Inicia o processo da planta (por exemplo, um simulador de planta industrial).
    -   Escuta conexões de clientes.
    -   Recebe comandos de controle dos clientes.
    -   Envia dados de feedback para os clientes.

-   **Cliente**:
    -   Conecta-se ao servidor.
    -   Envia comandos de controle para o servidor.
    -   Recebe dados de feedback do servidor.
    -   Exibe informações relevantes em um painel de controle (usando Python Dash).

## Requisitos

-   Python 3.x instalado.
-   Biblioteca `dash` instalada para o front end (painel de controle).

## Como Executar

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    cd seu-projeto
    ```

2. Execute o servidor:

    ```bash
    python main.py
    ```

3. Execute o cliente (em outro terminal ou máquina):

    ```bash
    python client.py
    ```

4. Acesse o painel de controle no navegador:

    ```
    http://localhost:8050
    ```

## Estrutura do Projeto

-   `server.py`: Implementação do servidor.
-   `client.py`: Implementação do cliente.
-   `main.py`: Painel de controle usando Python Dash.

## Observações

-   Certifique-se de ajustar as configurações de IP e porta conforme necessário.
-   Este é um exemplo simplificado. Em um cenário real, você pode precisar adicionar autenticação, segurança e escalabilidade.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.

---
