from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flaskblog import create_app

app = create_app()

migrate = Migrate(app)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
