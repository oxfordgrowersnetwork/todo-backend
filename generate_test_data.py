import datetime

import firebase_admin

from garden_todo_backend.add_task.add_task import FirestoreWrite, write_to_firestore_unlabelled
from garden_todo_backend.core.task import Task, Recurrence

example_project_string = 'demo-project'


def write_example_task(task: Task):
    write = FirestoreWrite(example_project_string, None, task.to_json())
    write_to_firestore_unlabelled(write)


firebase_admin.initialize_app()

# nonrepeating_task = Task('Non repeating task, any time', set(range(0, 12)), Recurrence.NEVER)
# write_example_task(nonrepeating_task)

# completed_non_repeating = Task('Non repeating task, any time, completed', set(range(0, 12)), Recurrence.NEVER)
# completed_non_repeating.last_completed = datetime.datetime.now()
# write_example_task(completed_non_repeating)

for month_index in range(0, 12):
    monthly_task = Task(f'Month{month_index} - not completed', {month_index}, Recurrence.MONTHLY)
    write_example_task(monthly_task)
    week_task = Task(f'Weekly task, m{month_index} - not completed', {month_index}, Recurrence.WEEKLY)
    write_example_task(monthly_task)

    monthly_task_completed = Task(f'Month{month_index} - not completed', {month_index}, Recurrence.MONTHLY)
    monthly_task_completed.last_completed = datetime.datetime.now()
    write_example_task(monthly_task_completed)

    week_task_completed = Task(f'Weekly task, m{month_index} - not completed', {month_index}, Recurrence.WEEKLY)
    week_task_completed.last_completed = datetime.datetime.now()
    write_example_task(week_task_completed)

yearly_task = Task('Late spring yearly task', {5, 6}, Recurrence.YEARLY)
write_example_task(yearly_task)

yearly_task_completed = Task('Late spring yearly task that is already done', {5, 6}, Recurrence.YEARLY)
yearly_task_completed.last_completed = datetime.datetime.now()
write_example_task(yearly_task_completed)
