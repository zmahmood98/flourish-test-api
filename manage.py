# import os
# from flask_migrate import Migrate

# from app import app, db


# app.config.from_object(os.environ['APP_SETTINGS'])

# migrate = Migrate(app, db)


# if __name__ == '__main__':
#     app.run()

import os
from flask_migrate import Migrate, MigrateCommand

from app import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)

migrate.add_command('db', MigrateCommand)


if __name__ == '__main__':
    migrate.run()
