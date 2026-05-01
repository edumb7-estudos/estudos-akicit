# Micro-API de Tarefas

Micro-API RESTful desenvolvida com FastAPI e SQLite para gerenciamento de tarefas. O projeto foi pensado como um MVP acadêmico com CRUD completo, testes automatizados e organização adequada para submissão no GitHub.

## Funcionalidades

- Criar tarefa
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefa
- Remover tarefa

## Tecnologias utilizadas

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pytest

## Como executar localmente

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o servidor:

```bash
uvicorn app.main:app --reload
```

4. Acesse:

- API: `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`

## Como executar os testes

```bash
pytest
```

## Exemplo de uso

### Criar tarefa

```json
POST /tasks
{
  "title": "Estudar FastAPI",
  "description": "Implementar CRUD de tarefas",
  "completed": false
}
```

### Resposta esperada

```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Implementar CRUD de tarefas",
  "completed": false,
  "created_at": "2026-04-26T00:00:00",
  "updated_at": "2026-04-26T00:00:00"
}
```

## Estrutura do projeto

```text
app/
  crud.py
  database.py
  main.py
  models.py
  schemas.py
tests/
  conftest.py
  test_tasks.py
requirements.txt
README.md
```

## Limitações e próximos passos

- O projeto usa SQLite local, sem autenticação e sem deploy online.
- Como evolução futura, pode receber filtros, paginação, autenticação e frontend web


## Como executar

pip install -r requirements.txt
uvicorn app.main:app --reload

## Licença

Uso acadêmico.
