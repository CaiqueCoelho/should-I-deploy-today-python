from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from repository import Repository
from flask import abort
import json

app = Flask(__name__)
api = Api(app)

class ShouldIDeployToday(Resource):
    def get(self, day):
        try:
            response = Repository().get(day)
        except Exception as e:
            abort(500, str(e))
        return response

    def put(self, day):
        try:
            data = json.loads(request.data)
            response = Repository().put(data['day'], data['shouldDeploy'])
        except Exception as e:
            abort(500, str(e))
        return response
    
    def delete(self, day):
        return abort(500, "Not implemented")
        # TODO

class ListDays(Resource):

    def post(self):
        try:
            data = json.loads(request.data)
            response = Repository().post(data['day'], data['shouldDeploy'])
        except Exception as e:
            abort(500, str(e))
        return response
    
    def get(self):
        try:
            response = Repository().getAll()
        except Exception as e:
            abort(500, str(e))
        return response
    
api.add_resource(ShouldIDeployToday, '/should-i-deploy-today/<string:day>')
api.add_resource(ListDays, '/should-i-deploy-today')

if __name__ == '__main__':
    app.run(debug=True)