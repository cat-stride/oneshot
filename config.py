# coding:utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	"""开发环境"""
	DEBUG = True
	# SQLALCHEMY_DATABASE_URI = 'mysql://root:123456789@localhost/' + os.path.join(basedir, 'develop')
	SQLALCHEMY_DATABASE_URI = 'mysql://test:test@localhost/oneshot'

class ProductionConfig(Config):
	"""生产环境"""
	SQLALCHEMY_DATABASE_URI = 'mysql://test:test@localhost/oneshot'
		
config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
