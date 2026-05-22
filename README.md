# RPA Web Audit Bot

Projeto de automação RPA desenvolvido em Python para simular uma auditoria web automatizada.

## Objetivo

O sistema lê uma planilha de entrada com registros fictícios, consulta os dados em um sistema web de teste, compara o status esperado com o status encontrado, salva evidências e gera um relatório final.

Este projeto foi criado como parte de um plano prático de desenvolvimento de portfólio, com foco em automação web, organização profissional de código, geração de relatórios e boas práticas de versionamento.

## Funcionalidades planejadas

- Leitura de planilha Excel
- Validação de dados de entrada
- Automação web com Selenium
- Consulta automática de registros
- Captura de evidências
- Geração de relatório final
- Registro de logs da execução
- Organização do projeto em camadas
- Preparação para publicação no GitHub

## Funcionalidades implementadas no Dia 1

- Criação da estrutura inicial do projeto
- Configuração do ambiente virtual Python
- Criação das pastas principais
- Criação do arquivo de configuração
- Criação do sistema de logs
- Criação automática da planilha de entrada
- Criação do arquivo `.gitignore`
- Criação do arquivo `.env.example`
- Preparação inicial do README

## Estrutura do projeto

```text
rpa-web-audit-bot/
│
├── app/
│   ├── main.py
│   ├── config.py
│   └── logger_config.py
│
├── data/
├── evidences/
├── logs/
├── output/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

## Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL
- Selenium
- WebDriver Manager
- Python Dotenv

## Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior
- Git
- Navegador Google Chrome ou Chromium

## Como executar no Linux

Clone o repositório ou acesse a pasta do projeto:

```bash
cd rpa-web-audit-bot
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python -m app.main
```

Caso o comando `python` não funcione, use:

```bash
python3 -m app.main
```

## Arquivo de entrada

No Dia 1, o sistema cria automaticamente uma planilha de entrada em:

```text
data/entrada.xlsx
```

A planilha contém registros fictícios com os seguintes campos:

```text
codigo
nome
status_esperado
```

Exemplo:

| codigo | nome           | status_esperado |
|--------|----------------|-----------------|
| 001    | Ana Silva      | Ativo           |
| 002    | João Souza     | Inativo         |
| 003    | Maria Lima     | Ativo           |
| 004    | Carlos Santos  | Pendente        |

## Logs

O projeto também cria um arquivo de log em:

```text
logs/execucao.log
```

Esse arquivo registra as principais etapas da execução da automação.

## Variáveis de ambiente

O arquivo `.env.example` contém as configurações principais do projeto:

```env
APP_NAME=rpa-web-audit-bot
INPUT_FILE=data/entrada.xlsx
OUTPUT_FILE=output/resultado_auditoria.xlsx
LOG_FILE=logs/execucao.log
EVIDENCE_DIR=evidences
```

Para usar variáveis reais no projeto, crie uma cópia com o nome `.env`:

```bash
cp .env.example .env
```

## Versionamento

Para iniciar o repositório Git:

```bash
git init
git add .
git commit -m "chore: create initial project structure"
```

## Status do projeto

Dia 1 concluído.

Nesta etapa, a base do projeto foi criada com ambiente virtual, dependências, estrutura de pastas, configuração inicial, sistema de logs e geração automática da planilha de entrada.

## Próximos passos

No Dia 2, o projeto será evoluído para leitura da planilha de entrada e validação dos dados antes da automação web.
