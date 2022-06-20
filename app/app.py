from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



if __name__ == '__main__':
    app.run(host='localhost')

app.config.from_object('config')

db = SQLAlchemy(app)
from models import user

import views

if __name__ == '__main__':
    app.run(host='localhost')
