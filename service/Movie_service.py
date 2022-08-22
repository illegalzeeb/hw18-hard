from dao.model.models import Movie
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list[Movie]:
        return self.movie_dao.get_all_movies()

    def get_movie_by_id(self, movie_id) -> list[Movie]:
        return self.movie_dao.get_movie_by_id(movie_id)

    def get_movie_by_genre(self, genre_id) -> list[Movie]:
        return self.movie_dao.get_movie_by_genre(genre_id)

    def get_movie_by_director(self, director_id) -> list[Movie]:
        return self.movie_dao.get_movie_by_director(director_id)

    def get_movie_by_year(self, year) -> list[Movie]:
        return self.movie_dao.get_movie_by_year(year)


    def post_movie(self, data):
        self.movie_dao.add_movie(**data)
        return None

    def put_movie(self, data):
        self.movie_dao.update_movie(**data)
        return None

    def del_movie(self, movie_id):
        self.movie_dao.delete_movie(movie_id)
        return None
