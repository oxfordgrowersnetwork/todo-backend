import pytest

from garden_todo_backend.add_task.add_task import get_task_from_json


def test_unpack_valid_request():
    input_object = {'project': 'exampleProject', 'task-name': 'Example task'}
    task = get_task_from_json(input_object)
    assert task.task_name == "Example task"


def test_unpack_invalid_request():
    input_object = {'project-name': 'exampleProject'}
    with pytest.raises(ValueError):
        get_task_from_json(input_object)
