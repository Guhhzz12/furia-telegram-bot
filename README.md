# FURIA Telegram Bot

Este repositório contém o código-fonte de um chatbot para o Telegram desenvolvido para interagir com fãs da FURIA, com o objetivo de responder perguntas e fornecer informações sobre a organização de esports.

## Funcionalidades

- O bot responde perguntas sobre a FURIA, principalmente sobre a equipe de CS:GO.
- O bot utiliza uma API para gerar respostas dinâmicas com base em perguntas feitas pelos usuários.
- O bot foi criado para fins educacionais e como parte de um projeto de entrevista de emprego.

## Como Usar

1. **Clone este repositório**:

   ```bash
   git clone https://github.com/Guhhzz12/furia-telegram-bot.git
   cd furia-telegram-bot
   ```

2. **Instale as dependências**

    Crie um ambiente virtual e instale as dependências com:

    ```bash
    pip install -r requirements.txt
    ```
3. **Configuração das Credenciais**

    As credencias do Telegram e da OpenRouterAPI devem ser definidas como variáveis de ambiente.

    - Token do Telegram: Crie um bot no BotFather e obtenha o seu token. Defina a variável de ambiente TELEGRAM_TOKEN com o seu token:

    ```bash
        export TELEGRAM_TOKEN = "seu_token_aqui"
    ```

    - Chave da OpenRouter API: Para utilizar a OpenRouter API, você precisa criar uma conta no OpenRouter e obter sua chave de API. Defina a variável de ambiente OPENROUTER_API_KEY com sua chave da API:

    ```bash
    OPENROUTER_API_KEY = "sua_chave_aqui"
    ```
4. **Rodar o bot com Docker**
    O projeto utiliza Docker para facilitar o deployment. Para rodar o bot dentro de um container Docker, execute o seguinte comando:
    ```bash
        docker build -t furia-telegram-bot .
        docker run -e TELEGRAM_TOKEN="seu_token_aqui" -e OPENROUTER_API_KEY="sua_chave_aqui" furia-telegram-bot
    ```
    Este comando vai construir a imagem Docker e iniciar o bot. O Docker irá automaticamente configurar o ambiente e as variáveis de ambiente.
5. **Interagir com o bot**
    Após rodar o bot, ele estará pronto para responder perguntas sobre a FURIA de CS:GO. Basta iniciar uma conversa no Telegram e interagir com o bot!

## Estrutura do Projeto
* bot.py: Arquivo principal que inicia o bot e gerencia a interação com o Telegram.

* Dockerfile: Arquivo de configuração para a construção da imagem Docker.

* Procfile: Arquivo utilizado para inciiar o bot quando hospedado em plataformas.

* ai_chat.py: Função para gerar respostas utilizando a OpenRouter API.

* requirements.txt: Lista das dependências necessárias para rodar o bot.
