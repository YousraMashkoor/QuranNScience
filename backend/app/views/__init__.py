from app.views.root import root_bp
from app.views.auth import Register

from flask_restful import Api
from flask import Blueprint


authenticate_bp = Blueprint('authenticate_bp', __name__)
authenticate_api = Api(authenticate_bp)

authenticate_api.add_resource(Register, '/user')

