from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db, setup_all

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    setup_all()
    manager.run()