# coding:utf-8
from . import db
from datetime import datetime

class ToDoList(db.Model):
	"""todolist table"""
	__tablename__ = 'todolist'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text, nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
	"""user table"""
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(10),nullable=False, index=True, unique=True)
	true_name = db.Column(db.String(10))
	sex = db.Column(db.String(2))
	birthday = db.Column(db.DateTime)
	location = db.Column(db.Text)
	email = db.Column(db.String(100),nullable=False, unique=True)
	signup_datetime = db.Column(db.DateTime)
	last_signin_datetime = db.Column(db.DateTime)
