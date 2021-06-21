from flask import jsonify
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity

from app import config

from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc


class Refresh(MethodResource, Resource):
    """The endpoint provides access to refresh a JWT token"""

    @doc(description='JWT token Refresh API',
         tags=['JWT Refresh'],
         params=config.PARAM_HEADER_AUTH
         )
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        refresh_token = create_refresh_token(identity=identity)
        return jsonify(access_token=access_token, refresh_token=refresh_token)

