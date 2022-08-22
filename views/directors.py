from flask_restx import Resource, Namespace

from dao.model.schema import DirectorSchema
from implemented import director_service
from service.Director_service import DirectorService

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')

class DirectorsView(Resource):
     def get(self):
        """
        Получение всех режисеров
        """
        return directors_schema.dump(director_service.get_directors()), 200

@directors_ns.route('/<int:director_id>')

class DirectorsView(Resource):
     def get(self, director_id):
        """
        Получение режисера по ид
        """
        return director_schema.dump(director_service.get_director_by_id(director_id)), 200