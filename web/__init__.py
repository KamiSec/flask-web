from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_pagedown import PageDown


db = SQLAlchemy()
mail = Mail()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    db.init_app(app)
    mail.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    return app

