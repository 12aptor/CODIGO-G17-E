from flask import Flask
from db import db
from flask_migrate import Migrate
from routes.users_routes import user_bp
from routes.auth_routes import auth_bp
from routes.products_routes import products_bp
from routes.sales_routes import sales_bp
from config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(products_bp, url_prefix='/api')
app.register_blueprint(sales_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)