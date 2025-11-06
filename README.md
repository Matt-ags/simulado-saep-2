# simulado-saep-2
Uma aplicação Django simples para gerenciamento de estoque de equipamentos eletrônicos.

Este repositório contém um projeto Django com duas aplicações principais:

- `estoque`: gerenciamento de produtos e histórico de alterações (adicionar, editar, remover, entradas/saídas)
- `usuario`: cadastro, login e logout de usuários

## Requisitos

- Python 3.11+ (ou outra versão compatível com Django 5.2.7)
- Virtualenv (recomendado)
- Dependências listadas em `requirements.txt` (Django 5.2.7)

## Instalação rápida (Windows / PowerShell)

1. Crie e ative um ambiente virtual

```powershell
python -m venv .venv
venv\Scripts\Activate
```

2. Instale dependências

```powershell
pip install -r requirements.txt
```

3. Aplique migrações e prepare o banco (SQLite por padrão)

```powershell
python manage.py makemigrations
```

```powershell
python manage.py migrate
```

4. (Opcional) Crie um superusuário para acessar o admin

```powershell
python manage.py createsuperuser
```

5. Execute o servidor de desenvolvimento

```powershell
python manage.py runserver
```

Abra http://127.0.0.1:8000/ no navegador.

## Como usar — visão geral

- Página principal (lista de produtos): rota definida na app `estoque` (ver templates em `estoque/templates/estoque/produtos.html`).
- Adicionar produto: formulário disponível via view `AddProduto` (template `adicionar_produto.html`).
- Editar produto: view `EditarProduto` reutiliza o mesmo template.
- Deletar produto: ação via `DeletarProduto` (registra histórico).
- Histórico: view `ListaHistorico` lista as ações registradas (criação, entrada, saída, exclusão).
- Autenticação: cadastro e login nas views em `usuario/views.py` (templates `templates/cadastro.html` e `templates/login.html`). Algumas operações exigem usuário autenticado.

## Estrutura principal do projeto

- `simulado_saep_2/` — configurações do projeto (inclui `settings.py`, usa SQLite por default)
- `estoque/` — app principal (models, views, forms, templates)
- `usuario/` — app de autenticação simples (cadastro/login)
- `templates/` — templates globais e base
- `static/` — arquivos estáticos (CSS)

## Observações

- Banco de dados padrão: `db.sqlite3` (arquivo na raiz do projeto).
- Dependências atuais: veja `requirements.txt`.

---

