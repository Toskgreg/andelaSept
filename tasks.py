import uuid
# This file contains code that manages your todo_list
todo_list = []
todos={}

# Write a function creates a task
class Task(object):
    ''' A Tasks class'''

    def __init__(
            self,
            task_id,
            task,
            status):
        ''' Initializes the question object'''
        self.task_id = task_id
        self.task = task
        self.status=status

  
    @staticmethod
    def create_task(task):
        """
        Adds the task (string value) to todo_list
        """
        todos['Id'] = uuid.uuid1()
        todos['task'] = task
        todos['status'] = 'pending'
        todo_list.append(todos)


# Write a function deletes a task

    @staticmethod
    def delete_task(task_id):
        """
        Removes the specified task from the todo_list
        """
        for task in todo_list:
            if task['Id'] == task_id:
                todo_list.pop()
                

# Write a function that marks a task finished

    @staticmethod
    def mark_as_finished(status):
        """
        Append the string label '[finished]' at the end of the task 
        if it does not already have the label appended.
        It should remain in the todo_list
        """
        for task in todo_list:
            if task['status'] == status:
                todos.update()
            

# Write a function deletes all tasks

    @staticmethod
    def delete_all_tasks():
        """
        Empty the the todo_lsit
        """
        todo_list.clear()