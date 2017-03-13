# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from config import config

db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	db.init_app(app)
	with app.app_context():
		db.create_all()
	moment = Moment(app)
	bootstrap = Bootstrap(app)
	# 路由
	# 自定义的错误页面

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)


	return app



