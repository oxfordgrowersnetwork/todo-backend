import pytest

from garden_todo_backend.add_task.add_task import get_project_key_from_json


def test_unpack_valid_request():
    input_object = {'project': 'exampleProject', 'task-name': 'Example task'}
    project = get_project_key_from_json(input_object)
    assert project == "exampleProject"


def test_unpack_invalid_request():
    input_object = {'task-name': 'Example task'}
    with pytest.raises(ValueError):
        get_project_key_from_json(input_object)
