# coding:utf-8
from flask import render_template,request,redirect,url_for,flash
from app.main import main
from app import crud

@main.route('/',methods=['GET','POST'])
@main.route('/index',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		data = {}
		content = request.form['anything']
		data['body'] = content
		# data['user_id'] = 1
		crud.create_todolist(data)
		return redirect(url_for('.index'))
	else:
		posts = crud.read_todolist()
		return render_template('index.html', posts=posts)
		