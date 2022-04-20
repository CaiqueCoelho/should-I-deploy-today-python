from flask_restful import Resource
from flask import abort

days = {
    'Monday': {
        'id': 0,
        'day': 'Monday', 
        'shouldDeploy': "yes"
    },
    'Friday': {
        'id': 1,
        'name': 'Friday',
        'shouldDeploy': "no"
    }
}

class Repository(Resource):

    def get(self, day):
        if day in days:
            return days[day]
        else:
            return abort(404)

    def getAll(self):
        return days

    def post(self, day, shouldDeploy):
        try:
            if day in days:
                days[day] = {
                    'id': days[day]['id'],
                    'day': day,
                    'shouldDeploy': shouldDeploy
                }
            else:
                days[day] = {
                    'id': len(days),
                    'day': day,
                    'shouldDeploy': shouldDeploy
                }

            return days[day]
        except Exception as e:
            abort(500, str(e))

    def put(self, day, shouldDeploy):
        try:
            return self.post(day, shouldDeploy)
        except Exception as e:
            abort(500, str(e))