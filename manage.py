from flask import Flask
from flask_migrate import Migrate
from flask.cli import FlaskGroup

from app import app, db, setup_all

migrate = Migrate(app, db)

def create_app():
    setup_all()
    return app

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    cli()