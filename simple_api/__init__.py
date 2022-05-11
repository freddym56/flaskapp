import os
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

PROJECT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
DATABASE_PATH = f'sqlite:////{PROJECT_PATH}/apps.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_PATH
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

from .models import Apps

class AppsSchema(ma.Schema):
    class Meta:
        fields = Apps.__table__.columns.keys()

apps_schema = AppsSchema()

@app.route('/')
def docs():
    # Just a small into page with API info
    response = {
        'Name': 'Simple API',
        'Version': '0.1',
        'end_points': {
            'name': '/apps',
            'params': {
                'page': 'Integer specifying page number.',
                'limit': 'Integer specifying number of items per page.'
            }
        }
    }
    return jsonify(response)

class GetApps(Resource):

    def get(self):
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 20, type=int)
        apps = Apps.query.paginate(page, limit)
        response = {
            'pagination': {
                'current_page': apps.page,
                'has_next': apps.has_next,
                'has_previous': apps.has_prev,
                'pages': apps.pages,
                'total': apps.total
            },
            'data': [apps_schema.dump(app) for app in apps.items]
        }
        return jsonify(response)

api.add_resource(GetApps, '/apps')
