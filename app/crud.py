from app.models import ToDoList, User
from . import db



# def create_todolist(tablename, data):
def create_todolist(data):
	todolist = ToDoList(body=data['body'])
	db.session.add(todolist)

def read_todolist():
	todolist = ToDoList.query.order_by(ToDoList.timestamp.desc()).all()
	return todolist

def update(tablename, data):
	pass

def delete(tablename, data):
	pass

