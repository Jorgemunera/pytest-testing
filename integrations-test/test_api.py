import requests
import uuid

ENDPOINT = "https://todo.pixegami.io/"

def create_task(body):
    return requests.put(ENDPOINT + "create-task", json=body)

def get_task(task_id):
    return requests.get(ENDPOINT + f"get-task/{task_id}")

def new_task_body(content="", user_id = uuid.uuid4().hex, is_done=False):
    return {
        "content": content,
        "user_id": user_id,
        "is_done": is_done
    }

def update_task(body):
    return requests.put(ENDPOINT + "update-task", json=body)

def get_tasks_by_user(user_id):
    return requests.get(ENDPOINT + f"list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"delete-task/{task_id}")


# TESTS
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    body = new_task_body("my content")

    res_new_task = create_task(body)
    parse_res_new_task = res_new_task.json()

    assert res_new_task.status_code == 200

    task_id = parse_res_new_task["task"]["task_id"]

    res_get_task = get_task(task_id)
    parse_res_get_task = res_get_task.json()

    assert res_get_task.status_code == 200
    assert parse_res_get_task["content"] == body["content"]
    assert parse_res_get_task["user_id"] == body["user_id"]


def test_can_update_task():
    body = new_task_body("my content", False)
    res_new_task = create_task(body)
    parse_res_new_task = res_new_task.json()

    assert res_new_task.status_code == 200

    task_id = parse_res_new_task["task"]["task_id"]
    user_id = parse_res_new_task["task"]["user_id"]

    body_changes = {
        "content": "update",
        "is_done": True,
        "user_id": user_id,
        "task_id": task_id
    }

    res_update_task = update_task(body_changes)

    assert res_update_task.status_code == 200

    res_get_task = get_task(task_id)
    parse_res_get_task = res_get_task.json()

    assert res_get_task.status_code == 200
    assert parse_res_get_task["content"] == body_changes["content"]
    assert parse_res_get_task["is_done"] == body_changes["is_done"]


def test_can_get_List_tasks_by_user():
    user_id = uuid.uuid4().hex
    n_tasks = 3
    for i in range(1,n_tasks +1 ):
        body = new_task_body(f"content {i}", user_id=user_id)
        res_new_task = create_task(body)
        assert res_new_task.status_code == 200
    
    res_get_tasks_by_user = get_tasks_by_user(user_id)
    parse_res_get_tasks_by_user = res_get_tasks_by_user.json()

    assert res_get_tasks_by_user.status_code == 200
    assert len(parse_res_get_tasks_by_user["tasks"]) == n_tasks

def test_can_delete_task():
    body = new_task_body("my content", False)
    res_new_task = create_task(body)
    parse_res_new_task = res_new_task.json()

    assert res_new_task.status_code == 200

    task_id = parse_res_new_task["task"]["task_id"]

    res_get_task = get_task(task_id)

    assert res_get_task.status_code == 200

    res_delete_task = delete_task(task_id)

    assert res_delete_task.status_code == 200

    res_get_task = get_task(task_id)

    assert res_get_task.status_code == 404
