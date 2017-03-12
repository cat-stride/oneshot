# coding:utf-8
from flask import render_template,request,redirect,url_for,flash
from app.main import main
from app import crud
from json

# index page
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
		

# request and response
@main.route('/api/bullets',methods=['GET','POST'])
def bullets():
	pass
	# if request.method == 'POST':
	# 	data = request.get_data()
	# 	body = json.loads(data)

	# 	crud.create_todolist(data)
	# 	return redirect(url_for('.index'))
	# else:
	# 	posts = crud.read_todolist()
	# 	return render_template('index.html', posts=posts)


#sign up
@main.route('/signup',methods=['GET','POST'])
def signup():
	pass

#sign in
@main.route('/signin',methods=['GET','POST'])
def signin():
	pass

