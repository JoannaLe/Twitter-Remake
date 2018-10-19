import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'words-in-fishbowl'
	SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'