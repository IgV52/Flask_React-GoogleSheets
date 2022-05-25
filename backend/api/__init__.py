from flask import Flask
from api.db import db
from api.google.routes import api_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='../../frontend/build', static_url_path='/')
    cors = CORS(app)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.before_first_request
    def create_table():
        db.create_all()

    @app.route('/')
    def index():
        return app.send_static_file('index.html')
        
    app.register_blueprint(api_bp, url_prefix='/api/gs')

    return app