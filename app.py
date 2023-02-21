from flask import Flask
from flask_restx import Api

from config import Config
from dao.director import Director
from dao.genre import Genre
from dao.movie import Movie
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):

    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    create_data(app, db)


def create_data(app, db):

    with app.app_context():
        db.create_all()

        d1 = Director(id=1, name='director1')
        d2 = Director(id=2, name='director2')
        d3 = Director(id=3, name='director3')
        d4 = Director(id=4, name='director4')

        g1 = Genre(id=1, name='genre1')
        g2 = Genre(id=2, name='genre2')
        g3 = Genre(id=3, name='genre3')
        g4 = Genre(id=4, name='genre4')

        m1 = Movie(id=1, title='title1', description='description1', trailer='trailer1', year=2011, rating='rating1',
                   genre_id=1, director_id=4)
        m2 = Movie(id=2, title='title2', description='description2', trailer='trailer2', year=2022, rating='rating2',
                   genre_id=2, director_id=3)
        m3 = Movie(id=3, title='title3', description='description3', trailer='trailer3', year=2016, rating='rating3',
                   genre_id=3, director_id=2)
        m4 = Movie(id=4, title='title4', description='description4', trailer='trailer4', year=2017, rating='rating4',
                   genre_id=4, director_id=1)
        m5 = Movie(id=5, title='title5', description='description5', trailer='trailer5', year=2022, rating='rating1',
                   genre_id=1, director_id=4)
        m6 = Movie(id=6, title='title6', description='description6', trailer='trailer6', year=2011, rating='rating2',
                   genre_id=2, director_id=3)
        m7 = Movie(id=7, title='title7', description='description7', trailer='trailer7', year=2019, rating='rating3',
                   genre_id=3, director_id=2)
        m8 = Movie(id=8, title='title8', description='description8', trailer='trailer8', year=2016, rating='rating4',
                   genre_id=4, director_id=1)

        with db.session.begin():
            db.session.add_all([d1, d2, d3, d4])
            db.session.add_all([g1, g2, g3, g4])
            db.session.add_all([m1, m2, m3, m4, m5, m6, m7, m8])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
