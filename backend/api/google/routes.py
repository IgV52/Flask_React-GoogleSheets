from api.google.resources import GoogleSheets
from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(GoogleSheets, '/')