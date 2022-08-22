from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.Director_service import DirectorService
from service.Genre_service import GenreService
from service.Movie_service import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao=genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao=director_dao)