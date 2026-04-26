def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Micro-API de tarefas em funcionamento."}


def test_create_task(client):
    payload = {
        "title": "Estudar FastAPI",
        "description": "Criar rotas CRUD para o projeto",
        "completed": False,
    }

    response = client.post("/tasks", json=payload)
    body = response.json()

    assert response.status_code == 201
    assert body["title"] == payload["title"]
    assert body["description"] == payload["description"]
    assert body["completed"] is False
    assert "id" in body


def test_list_tasks_returns_created_items(client):
    client.post("/tasks", json={"title": "Task 1", "description": "Primeira", "completed": False})
    client.post("/tasks", json={"title": "Task 2", "description": "Segunda", "completed": True})

    response = client.get("/tasks")
    body = response.json()

    assert response.status_code == 200
    assert len(body) == 2
    assert body[0]["title"] == "Task 1"
    assert body[1]["title"] == "Task 2"


def test_get_task_by_id(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Documentar API", "description": "Escrever README", "completed": False},
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Task antiga", "description": "Texto inicial", "completed": False},
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Task atualizada", "completed": True},
    )
    body = response.json()

    assert response.status_code == 200
    assert body["title"] == "Task atualizada"
    assert body["completed"] is True
    assert body["description"] == "Texto inicial"


def test_delete_task(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Task para remover", "description": "Excluir depois", "completed": False},
    )
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    fetch_response = client.get(f"/tasks/{task_id}")

    assert delete_response.status_code == 204
    assert fetch_response.status_code == 404
    assert fetch_response.json()["detail"] == "Task not found"


def test_returns_404_for_unknown_task(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

