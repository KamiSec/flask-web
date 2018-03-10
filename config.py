import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = "qewtd34yAjt5gj324"
SQLALCHEMY_TRACK_MODIFICATIONS = False
FLASKY_POSTS_PER_PAGE = 30
FLASKY_FOLLOWERS_PER_PAGE = 20
FLASKY_COMMENTS_PER_PAGE = 20
FLASKY_MAIL_SUBJECT_PREFIX = 'KamiSec'
FLASKY_MAIL_SENDER = 'KamiSec <test@qq.com>'
FLASKY_ADMIN ='admin@qq.com'
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'admin@qq.com'
MAIL_PASSWORD = ''
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:passwd@localhost:3306/flask'
