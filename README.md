# RPA Web Audit Bot com BotCity

Projeto de automação RPA desenvolvido em Python para simular uma auditoria web baseada em planilhas Excel.

O robô lê uma planilha de entrada, consulta automaticamente registros em uma página web local, compara o status esperado com o status encontrado, salva evidências visuais em PNG e gera um relatório final em Excel com os resultados da auditoria.

---

## Objetivo do projeto

O objetivo deste projeto é demonstrar uma automação RPA completa, com leitura de dados, interação com navegador, validação de informações, geração de evidências e criação de relatório final.

O fluxo simula um cenário comum em empresas, onde é necessário verificar se informações registradas em uma planilha estão de acordo com os dados exibidos em um sistema web.

---

## Tecnologias utilizadas

- Python 3.11
- BotCity Web
- Selenium/WebDriver
- Pandas
- OpenPyXL
- WebDriver Manager
- python-dotenv
- HTML
- CSS
- JavaScript
- Git e GitHub

---

## Funcionalidades

- Leitura automática de planilha Excel.
- Validação de colunas obrigatórias.
- Validação de campos vazios.
- Consulta automática de registros em página web.
- Integração com BotCity Web.
- Captura de evidências em PNG.
- Comparação entre status esperado e status encontrado.
- Classificação dos registros como:
  - Conforme
  - Não conforme
  - Não encontrado
  - Erro
- Tratamento de erro por registro.
- Geração de relatório Excel final.
- Criação de aba de resumo no relatório.
- Formatação automática do relatório.
- Abertura automática do relatório no Windows.
- Registro de logs da execução.

---

## Estrutura do projeto

```text
rpa-web-audit-bot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── logger_config.py
│   ├── excel_reader.py
│   ├── sample_data_service.py
│   ├── botcity_automation.py
│   ├── audit_service.py
│   └── report_service.py
├── data/
│   └── entrada.xlsx
├── evidences/
│   ├── evidencia_001.png
│   ├── evidencia_002.png
│   ├── evidencia_003.png
│   ├── evidencia_004.png
│   └── evidencia_999.png
├── logs/
│   └── execucao.log
├── output/
│   └── resultado_auditoria.xlsx
├── web/
│   └── index.html
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## Fluxo da automação

```text
1. O sistema cria uma planilha de entrada de exemplo.
2. A planilha é lida e validada.
3. Os códigos são extraídos da planilha.
4. O BotCity abre a página web local.
5. Cada código é consultado automaticamente.
6. O robô captura nome, status e mensagem da tela.
7. Uma evidência visual é salva em PNG.
8. Os dados esperados são comparados com os dados encontrados.
9. O resultado é classificado.
10. Um relatório Excel final é gerado.
11. O relatório é aberto automaticamente no Windows.
12. Um resumo final é exibido no terminal.
```

---

## Exemplo de entrada

A planilha de entrada possui as seguintes colunas:

```text
codigo
nome
status_esperado
```

Exemplo:

| codigo | nome              | status_esperado |
|-------:|-------------------|-----------------|
| 001    | Ana Silva         | Ativo           |
| 002    | João Souza        | Inativo         |
| 003    | Maria Lima        | Inativo         |
| 004    | Carlos Santos     | Pendente        |
| 999    | Registro Fantasma | Ativo           |

---

## Exemplo de saída

O relatório final é gerado em:

```text
output/resultado_auditoria.xlsx
```

A aba principal contém:

| codigo | nome_esperado     | nome_encontrado | status_esperado | status_encontrado | resultado_auditoria |
|-------:|-------------------|-----------------|-----------------|-------------------|---------------------|
| 001    | Ana Silva         | Ana Silva       | Ativo           | Ativo             | Conforme            |
| 002    | João Souza        | João Souza      | Inativo         | Inativo           | Conforme            |
| 003    | Maria Lima        | Maria Lima      | Inativo         | Ativo             | Não conforme        |
| 004    | Carlos Santos     | Carlos Santos   | Pendente        | Pendente          | Conforme            |
| 999    | Registro Fantasma | -               | Ativo           | -                 | Não encontrado      |

A aba de resumo apresenta:

```text
Total de registros: 5
Total conforme: 3
Total não conforme: 1
Total não encontrado: 1
Total erro: 0
```

---

## Evidências

Para cada consulta, o robô salva uma evidência visual na pasta:

```text
evidences/
```

Exemplos:

```text
evidences/evidencia_001.png
evidences/evidencia_002.png
evidences/evidencia_003.png
evidences/evidencia_004.png
evidences/evidencia_999.png
```

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/rpa-web-audit-bot.git
cd rpa-web-audit-bot
```

### 2. Criar ambiente virtual

No Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 4. Executar a automação

```powershell
python -m app.main
```

---

## Resultado esperado

Ao executar o projeto, o robô deve:

```text
Criar a planilha de entrada
Ler e validar os dados
Abrir a página web local
Consultar todos os registros
Salvar evidências em PNG
Comparar esperado x encontrado
Gerar relatório Excel
Abrir o relatório automaticamente
Exibir resumo final no terminal
```

---

## Principais aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Automação RPA.
- Automação web com BotCity.
- Manipulação de planilhas Excel.
- Geração de relatórios.
- Captura de evidências.
- Tratamento de erros.
- Separação de responsabilidades.
- Organização modular de projeto Python.
- Logs de execução.
- Versionamento com Git.

---

## Possíveis melhorias futuras

- Ler uma planilha real fornecida pelo usuário.
- Permitir configuração do caminho da planilha via `.env`.
- Adicionar interface gráfica simples.
- Enviar relatório por e-mail automaticamente.
- Integrar com banco de dados.
- Executar a automação de forma agendada.
- Gerar relatório em PDF.
- Publicar evidências em uma pasta compartilhada.

---

## Autor

Desenvolvido por Mateus como projeto de portfólio em automação RPA com Python e BotCity.
