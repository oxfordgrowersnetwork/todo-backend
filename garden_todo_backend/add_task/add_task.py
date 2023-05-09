from firebase_admin import firestore

from garden_todo_backend.core.task import Recurrence
from garden_todo_backend.core.task import Task

PROJECT_KEY = 'project'
TASK_NAME_KEY = 'task-name'


def add_task(request_body):
    data_to_store = build_firestore_write(request_body)
    write_to_firestore(data_to_store)
    return 'Added task'


def build_firestore_write(request_body):
    if request_body is None:
        raise ValueError('Request must be JSON')

    project = get_project_key_from_json(request_body)
    task = get_task_from_json(request_body)
    return FirestoreWrite(project, task.task_name, task.__dict__)


class FirestoreWrite:
    def __init__(self, collection_name, document_name, data):
        self.collection_name = collection_name
        self.document_name = document_name
        self.data = data


def write_to_firestore(data_to_write: FirestoreWrite):
    db = firestore.client()

    project_collection = get_project(db, data_to_write.collection_name)
    project_collection.document(data_to_write.document_name).set(data_to_write.data)


def get_project_key_from_json(json_object):
    if PROJECT_KEY not in json_object:
        raise ValueError(f'Missing essential information: {PROJECT_KEY}')
    return json_object[PROJECT_KEY]


def get_task_from_json(json_object):
    if TASK_NAME_KEY not in json_object:
        raise ValueError(f'Missing essential information: {TASK_NAME_KEY}')
    return Task(json_object[TASK_NAME_KEY], set(range(0, 12)), Recurrence.NEVER)


def get_project(firebase_db, project):
    collection_ref = firebase_db.collection(project)
    example_task_from_collection = collection_ref.limit(1).get()
    if not example_task_from_collection:
        raise ValueError(f'Project does not exist {project}')
    return collection_ref
