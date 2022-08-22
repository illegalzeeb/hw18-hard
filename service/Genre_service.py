from dao.model.models import Genre
from dao.genre import GenreDAO


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> list[Genre]:
        return self.genre_dao.get_all_genres()

    def get_genre_by_id(self, genre_id) -> list[Genre]:
        return self.genre_dao.get_genre_by_id(genre_id)
