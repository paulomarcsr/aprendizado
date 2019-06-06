from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.Category import CategoryResource
from resources.Comment import CommentResource
from flask_cors import CORS, cross_origin



api_bp = Blueprint('api', __name__)
api = Api(api_bp)


CORS(api_bp)


# Route

api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
