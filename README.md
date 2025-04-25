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

    O arquivo config.py foi configurado para não incluir credenciais sensíveis. Você deve inserir suas credenciais manualmente.

    Token do Telegram: Crie um bot no BotFather e obtenha o seu token.

    Abra o arquivo config.py e insira o token gerado no campo:
    ```python
        TELEGRAM_TOKEN = "seu_token_aqui"
    ```

    Chave da OpenRouter API: Para utilizar a OpenRouter API, você precisa criar uma conta no OpenRouter e obter sua chave de API.

    Após isso, insira a chave da API no arquivo config.py:
    ```python
    OPENROUTER_API_KEY = "sua_chave_aqui"
    ```
4. **Rodar o bot**
    Depois de inserir suas credenciais, você pode rodar o bot localmente com o seguinte comando:
    ```bash
    python bot.py
    ```
5. **Interagir com o bot**
    Após rodar o bot, ele estará pronto para responder perguntas sobre a FURIA de CS:GO. Basta iniciar uma conversa no Telegram e interagir com o bot!

## Estrutura do Projeto
* bot.py: Arquivo principal que inicia o bot e gerencia a interação com o Telegram.

* config.py: Contém as credenciais e as configurações do bot. As credenciais devem ser inseridas manualmente.

* openai_chat.py: Função para gerar respostas utilizando a OpenRouter API.

* requirements.txt: Lista das dependências necessárias para rodar o bot.
