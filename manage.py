#!/usr/bin/env python3
import os
from web import create_app, db
from web.models import User, Role, Permission, Post
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_debugtoolbar import DebugToolbarExtension

app = create_app()
manager = Manager(app)
toolbar = DebugToolbarExtension(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()

