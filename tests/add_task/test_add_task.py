import pytest

from garden_todo_backend.add_task.add_task import build_firestore_write


def test_build_firestore_write():
    request = {'project': 'test-project', 'task-name': 'Example task'}
    data_to_write = build_firestore_write(request)
    assert data_to_write.collection_name == 'test-project'
    assert data_to_write.document_name == 'Example task'
    assert data_to_write.data['task_name'] == 'Example task'


def test_build_firestore_write_with_non_json_request():
    with pytest.raises(ValueError):
        build_firestore_write(None)
