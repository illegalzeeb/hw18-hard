from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, movie_id):
        return self.session.query(Movie).filter(Movie.id == movie_id).one()

    def get_movie_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def add_movie(self, **kwargs):
        self.session.add(Movie(**kwargs))
        return None

    def update_movie(self, **kwargs):
        self.session.query(Movie).filter(kwargs.get('id').update(kwargs) == Movie.id)
        self.session.commit()
        return None

    def delete_movie(self, movie_id):
        self.session.query(Movie).filter(Movie.id == movie_id).delete()
        self.session.commit()
        return None
