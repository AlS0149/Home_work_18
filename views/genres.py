from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):

        result = genre_service.get_all()
        if result:
            return genres_schema.dump(result), 200
        else:
            return "Данные не найдены", 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):

        result = genre_service.get_one(gid)
        if result:
            return genre_schema.dump(result), 200
        else:
            return "Данные не найдены", 404
