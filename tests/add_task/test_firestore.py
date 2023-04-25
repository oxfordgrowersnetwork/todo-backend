import firebase_admin
import pytest
from google.cloud import firestore

from garden_todo_backend.add_task.add_task import write_to_firestore, FirestoreWrite, add_task

exampleProjectName = 'exampleProject'


@pytest.fixture(scope="session", autouse=True)
def initalize_firebase_app():
    firebase_admin.initialize_app()


@pytest.fixture(scope="function")
def firestore_client():
    client = firestore.Client()

    for collection in client.collections():
        print(collection.id)

    # Verify we are not connected to production
    assert not any(client.collections())

    # Create project in the firestore
    db = client.collection(exampleProjectName)
    db.document("TASK").set({})

    yield client

    documents = client.collection(exampleProjectName).list_documents()
    for document in documents:
        document.delete()


def test_write_to_firestore(firestore_client):
    data = {'task_name': 'Example task'}

    data_to_write = FirestoreWrite(collection_name=exampleProjectName, document_name="Example task", data=data)
    write_to_firestore(data_to_write)

    db = firestore_client.collection(exampleProjectName)
    retrieved_data = db.document("Example task").get().to_dict()
    assert retrieved_data == data


def test_write_to_firestore_with_invalid_projects_raises_error(firestore_client):
    data = {'task_name': 'Example task'}

    data_to_write = FirestoreWrite(collection_name="invalidProject", document_name="Example task", data=data)
    with pytest.raises(ValueError):
        write_to_firestore(data_to_write)


def test_add_task(firestore_client):
    request_data = {'project': exampleProjectName, 'task-name': 'Example task'}

    add_task(request_data)
    db = firestore_client.collection(exampleProjectName)
    retrieved_data = db.document("Example task").get().to_dict()
    assert retrieved_data == {'task_name': 'Example task'}
