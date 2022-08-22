from flask_restx import Resource, Namespace

from dao.model.schema import GenreSchema
from implemented import genre_service
from service.Genre_service import GenreService

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')

class GenresView(Resource):
     def get(self):
        """
        Получение всех жанров
        """
        return genres_schema.dump(genre_service.get_genres()), 200

@genres_ns.route('/<int:genre_id>')

class GenresView(Resource):
     def get(self, genre_id):
        """
        Получение жанра по ид
        """
        return genre_schema.dump(genre_service.get_genre_by_id(genre_id)), 200