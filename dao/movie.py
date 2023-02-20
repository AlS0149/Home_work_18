from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):

        return self.session.query(Movie).all()

    def get_one(self, mid):

        return self.session.query(Movie).get(mid)

    def get_by_did(self, did):

        return self.session.query(Movie).filter(Movie.director_id == int(did)).all()

    def get_by_gid(self, gid):

        return self.session.query(Movie).filter(Movie.genre_id == int(gid)).all()

    def get_by_year(self, year):

        return self.session.query(Movie).filter(Movie.year == int(year)).all()

    def create(self, data):

        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):

        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
