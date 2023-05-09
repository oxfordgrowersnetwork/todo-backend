import firebase_admin

from garden_todo_backend.add_task.add_task import FirestoreWrite, write_to_firestore_unlabelled
from garden_todo_backend.core.task import Task, Recurrence

example_project_string = 'demo-project'


def write_example_task(task: Task):
    write = FirestoreWrite(example_project_string, None, task.to_json())
    write_to_firestore_unlabelled(write)


firebase_admin.initialize_app()

nonrepeating_task = Task('Non repeating task, any time', set(range(0, 12)), Recurrence.NEVER)
write_example_task((nonrepeating_task))
