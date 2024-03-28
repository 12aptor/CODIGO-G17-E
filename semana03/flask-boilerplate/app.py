from flask import Flask
from db import db
from flask_migrate import Migrate
from controllers.users_controller import UserController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Flask is running! 🤠'

@app.route('/users')
def getUsers():
    controller = UserController()
    return controller.getAll()

@app.route('/users/<int:id>')
def getUserById(id):
    controller = UserController()
    return controller.getById(id)

if __name__ == '__main__':
    app.run(debug=True)