# Configuração do Ambiente para o Projeto

Este documento descreve como configurar o ambiente necessário para executar o projeto.

## Pré-requisitos

- **Python 3.12**: Certifique-se de que o Python 3.12 está instalado no sistema.
- **UV**: Ferramenta de gerenciamento de dependências para Python.

## Passos para Configuração

### 1. Instalar o Python 3.12

1. Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Faça o download do instalador para Python 3.12.
3. Siga as instruções de instalação de acordo com o seu sistema operacional.
4. Verifique a instalação:
   ```bash
   python --version
   ```
   Ou, caso o comando acima não funcione:
   
   ```bash
   python --version
   ```

### 2. Instalar o UV

1. Instale o UV utilizando o pip:

   ```bash
   pip install uv
   ```

2. Verifique a instalação do UV:

   ```bash
   uv --version
   ```

### 3. Inicializar o Projeto

1. Navegue até o diretório do projeto:

   ```bash
   cd /caminho/para/seu/projeto
   ```

2. Inicie o projeto com o UV:

   ```bash
   uv init
   ```

### 4. Adicionar Dependências

1. No arquivo pyproject.toml, inclua as dependências necessárias na seção [dependencies]:

   ```bash
   dependencies = [
    "guardrails-ai==0.6.0",
    "guardrails-api-client==0.4.0a1",
    "openai>=1.57.0",
    "openpyxl>=3.1.5",
    "pandas>=2.2.3",
    "python-dotenv>=1.0.1",
    ]
   ```

2. Sincronize as dependências com o comando:

   ```bash
   uv sync
   ```

### 5. Configurar Variáveis de Ambiente

1. Crie um arquivo .env na raiz do projeto:

   ```bash
   touch .env
   ```

2. Adicione a chave da API da OpenAI ao arquivo .env:

   ```bash
   OPENAI_API_KEY=sua-chave-api-aqui
   ```
