from peewee import *

db = SqliteDatabase('tasks.db')
class Task(Model):
    name = CharField()
    done = BooleanField()
    class  Meta:
        database = db

def get_task():
    tasks = [(task.name,task.done) for task in Task.select()]
    return tasks

def delete(id):
    Task.delete_by_id(id)
def update(id,data):
    try:
        task = Task.get_by_id(id)
        task.name = data['name']
        task.done = data['done']
        task.save()
        return f"task {task.name}, done = {task.done}"
    except  DoesNotExist:
        return 'task does not exist'
