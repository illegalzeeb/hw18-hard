
from flask_restx import Resource, Namespace
from flask import request
from dao.model.schema import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Получение фильмов
        """
        if director_id := request.args.get('director_id'):
            return movies_schema.dump(movie_service.get_movie_by_director(director_id=director_id)), 200
        elif genre_id := request.args.get('genre_id'):
            return movies_schema.dump(movie_service.get_movie_by_genre(genre_id=genre_id)), 200
        elif year := request.args.get('year'):
            return movies_schema.dump(movie_service.get_movie_by_year(year=year)), 200
        elif movie_id := request.args.get('movie_id'):
            return movies_schema.dump(movie_service.get_movie_by_id(movie_id=movie_id)), 200
        else:
            return movies_schema.dump(movie_service.get_movies()), 200

    def post(self):
        """
         Добавление фильмов
         """
        movie_service.post_movie(request.json)
        return "", 201

    def put(self):
        """
         Обновление фильмов
         """
        movie_service.put_movie(request.json)
        return "", 200

    def delete(self, movie_id):
        """
         Удаление фильмов
         """
        movie_service.del_movie(movie_id)
        return "", 204
