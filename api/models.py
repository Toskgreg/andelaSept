from flask import jsonify, request
import json
import re
import uuid

tasks = []


class Tasks:
    def __init__(self, task_id, details,status):
        self.task_id = task_id
        self.details = details
        self.status=status
        

    @staticmethod
    def create_task():
        x = request.get_json()

        details = x.get('details')
        task_id=uuid.uuid1()
        status='pending'

        if not details or details.isspace():
            return jsonify({"message": "Enter a task"}), 400
        task = Tasks(task_id, details,status)
        tasks.append(task)
        return jsonify({
            'Id': task_id,
            'task': task.__dict__,
            'message': 'Success'}), 201

    @staticmethod
    def delete_task(task_id):
        """
        Removes the specified task from the task_list
        """
        for task in tasks:
            if task['Id'] == task_id:
                tasks.pop()

    @staticmethod
    def delete_all_tasks():
        """
        Empty the the todo_lsit
        """
        tasks.clear()

    @staticmethod
    def mark_as_finished(task_id,status):
        """
        Append the string label '[finished]' at the end of the task 
        if it does not already have the label appended.
        It should remain in the todo_list
        """
        for task in tasks:
            if task['Id'] == task_id:
                status='finished'
                task.update()

    @staticmethod
    def mark_as_unfinished(task_id,status):
        """
        Append the string label '[finished]' at the end of the task 
        if it does not already have the label appended.
        It should remain in the todo_list
        """
        for task in tasks:
            if task['Id'] == task_id:
                status='pending'
                task.update()

