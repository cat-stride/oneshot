# coding:utf-8
#!/usr/bin/env python

from app import create_app, db
from app.models import User, Bullet
from flask_script import Manager, Shell

app = create_app('default')
manager = Manager(app)

def make_shell_context():
	return dict(app=app, db=db, User=User, Bullet=Bullet)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
	with app.app_context():      # 这两句要加 不然会出现 relation does not exist 报错
		db.create_all()  		 # 或者提前建好表应该也可以
	manager.run()
