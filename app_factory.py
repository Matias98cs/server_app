import os
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from config import db_connector, db_user, db_password, db_ip_address, db_name
from src.models.base import db
from src.routes.routes_articulosweb import articulos_web_bp
from src.routes.routes_categoriasweb import categorias_web_bp
from src.routes.routes_ofertas import ofertas_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{db_connector}://{db_user}:{db_password}@{db_ip_address}/{db_name}"
    db.init_app(app)
    # csrf.init_app(app)
    CORS(app, resources={
         r"//*": {"origins": "http://localhost:5173", "methods": "GET" "POST" "PUT" "DELETE"}})

    with app.app_context():
        db.create_all()

    app.register_blueprint(articulos_web_bp)
    app.register_blueprint(categorias_web_bp)
    app.register_blueprint(ofertas_bp)

    return app
