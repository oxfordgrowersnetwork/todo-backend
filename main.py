import firebase_admin
import flask
import functions_framework

import garden_todo_backend.add_task.add_task


# Deploy command: gcloud functions deploy add-task --gen2 --region europe-west2 --runtime python311 --source . --entry-point add_task_request


@functions_framework.http
def add_task_request(request: flask.Request):
    firebase_admin.initialize_app()
    return garden_todo_backend.add_task.add_task.add_task(request.get_json())
