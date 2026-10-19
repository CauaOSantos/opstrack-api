# OpsTrack API

A **OpsTrack API** é uma API desenvolvida em Python com Flask para simular o gerenciamento de chamados e informações de um serviço. O projeto também utiliza ferramentas de qualidade de código para manter um padrão durante o desenvolvimento.

## 1. Pré-requisitos

Antes de começar, é necessário ter instalado:

- [Python](https://www.python.org/)
- [Git](https://git-scm.com/)
- VS Code (opcional, mas recomendado)

Para verificar se estão instalados:

```bash
python --version
git --version
```

## 2. Configurando o ambiente

### 1. Clone o repositório

```bash
git clone https://github.com/matvieira7/opstrack-api.git
```

### 2. Acesse a pasta do projeto

```bash
cd opstrack-api
```

### 3. Crie o ambiente virtual

No Windows:

```powershell
python -m venv venv
```

### 4. Ative o ambiente virtual

No PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

No Prompt de Comando:

```cmd
venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Instale o pre-commit

```bash
pip install pre-commit
```

### 7. Instale o hook

```bash
pre-commit install
```

Após essa etapa, o hook estará configurado na máquina.

Para verificar se o pre-commit está instalado:

```bash
pre-commit --version
```

O Flake8 será executado automaticamente antes de cada commit.

## 3. Executando a aplicação

Com o ambiente virtual ativado, execute:

```bash
python app.py
```

A API estará disponível em:

```text
http://127.0.0.1:5000
```

Abra esse endereço no navegador para testar a aplicação.

## 4. Qualidade de código

O projeto utiliza o **Flake8** para verificar problemas de estilo e possíveis erros no código Python.

Para executar o Flake8 manualmente:

```bash
flake8
```

Para verificar a versão instalada:

```bash
flake8 --version
```

### Pre-commit

O projeto utiliza o **pre-commit** para executar o Flake8 automaticamente antes de cada commit.

O fluxo funciona da seguinte forma:

```text
git commit
    ↓
pre-commit
    ↓
Flake8
    ↓
┌─────────────────────┐
│ Código sem erros?   │
└─────────────────────┘
       ↓        ↓
      SIM      NÃO
       ↓        ↓
   Commit     Commit
   realizado  bloqueado
```

Se o Flake8 encontrar algum erro, o commit será bloqueado. Nesse caso, os problemas devem ser corrigidos antes de realizar o commit novamente.

## 5. Como contribuir

O projeto utiliza um fluxo de trabalho baseado em **branches, Conventional Commits e Pull Requests**.

### 1. Crie uma nova branch

A partir da `main`:

```bash
git checkout main
git pull origin main
git checkout -b feature/nome-da-alteracao
```

Exemplo:

```bash
git checkout -b feature/qualidade-codigo
```

### 2. Faça as alterações

Implemente a funcionalidade, correção ou documentação necessária.

### 3. Adicione os arquivos

```bash
git add .
```

### 4. Faça o commit

Utilize o padrão **Conventional Commits**:

```bash
git commit -m "feat: adiciona nova funcionalidade"
```

Exemplos:

```text
feat: adiciona endpoint de chamados
fix: corrige resposta do endpoint
docs: atualiza README
chore: configura pre-commit
```

O pre-commit executará o Flake8 automaticamente antes de finalizar o commit.

### 5. Envie a branch para o GitHub

```bash
git push -u origin feature/nome-da-alteracao
```

### 6. Abra um Pull Request

Após enviar a branch para o GitHub, abra um **Pull Request** direcionando a branch de desenvolvimento para a `main`.

O fluxo de contribuição é:

```text
main
  │
  └──→ feature/nova-alteracao
           │
           ├── alterações
           ├── git add
           ├── commit
           └── push
                    │
                    ↓
             Pull Request
                    │
                    ↓
                  main
```

As alterações devem ser integradas à `main` por meio de Pull Requests, evitando alterações diretas na branch principal.

## Rodando os testes

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements-dev.txt
pytest -v
```

## Rodando os testes

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements-dev.txt
pytest -v
```

## Cobertura de testes

A equipe definiu como meta mínima **85%** de cobertura.

```bash
pytest --cov=app --cov-fail-under=85
```

