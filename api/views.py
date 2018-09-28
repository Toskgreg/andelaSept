from flask import Flask, request, jsonify
import json
# import uuid
from api.models import Tasks,tasks
from api.auth import SignUp,Users,user

app = Flask(__name__)


@app.route('/api/v1/auth/register', methods=['POST'])
def post_user():
    return SignUp.create_user()
@app.route('/api/v1/auth/login', methods=['POST'])
def login_user():
    return SignUp.login()
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout_user():
    return SignUp.logOut()
@app.route('/api/v1/tasks', methods=['POST'])
def post_task():
    return Tasks.create_task()
@app.route('/api/v1/tasks', methods=['DELETE'])
def delete_all_tasks():
    return Tasks.delete_all_tasks()
@app.route('/api/v1/questions/<int:task_id>/finished', methods=['PUT'])
def mark(task_id,status):
    return Tasks.mark_as_finished(task_id,status)
@app.route('/api/v1/questions/<int:task_id>/unfinished', methods=['PUT'])
def unmark(task_id,status):
    return Tasks.mark_as_unfinished(task_id,status)
@app.route('/api/v1/task/<int:task_id>', methods=['DELETE'])
def single_task(task_id):
    return Tasks.delete_task(task_id)