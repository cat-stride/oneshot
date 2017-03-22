import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'my soul was a light blue dress the color of the sky'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = 25
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'catstride@163.com'
	MAIL_PASSWORD = 'oneshot321'       # 163邮箱的话这里要填授权码
	MAIL_SUBJECT_PREFIX = '[OneShot]'
	MAIL_SENDER = 'OneShot Team <catstride@163.com>'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	# SQLALCHEMY_DATABASE_URI = 'mysql://root:123456789@localhost/' + os.path.join(basedir, 'develop')
	# SQLALCHEMY_DATABASE_URI = 'mysql://test:test@localhost/oneshot'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456789@localhost/oneshot'
	# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Shippo:fighting2017@localhost/Shippo'

class ProductionConfig(Config):
	# SQLALCHEMY_DATABASE_URI = 'mysql://test:test@localhost/oneshot'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456789@localhost/oneshot'
	
config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
