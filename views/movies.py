from flask import request
from flask_restx import Resource, Namespace

from dao.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):

        did = request.args.get('director_id')
        gid = request.args.get('genre_id')
        year = request.args.get('year')

        if did is None and gid is None and year is None:
            result = movie_service.get_all()
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

        elif did and gid is None and year is None:
            result = movie_service.get_by_did(did)
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

        elif gid and did is None and year is None:
            result = movie_service.get_by_gid(gid)
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

        elif year and gid is None and did is None:
            result = movie_service.get_by_year(year)
            if result:
                return movies_schema.dump(result), 200
            else:
                return "Данные не найдены", 404

    def post(self):

        try:
            data = request.json
            movie_service.create(data)
            return '', 201
        except Exception as e:
            return str(e), 404


@movie_ns.route('/<int:mid>')  # Представление по маршруту /movies/mid
class MovieView(Resource):

    def get(self, mid):

        result = movie_service.get_one(mid)
        if result:
            return movie_schema.dump(result), 200
        else:
            return "Данные не найдены", 404

    def put(self, mid):

        try:
            data = request.json
            data['id'] = mid
            movie_service.update(data)
            return '', 204
        except Exception as e:
            return str(e), 404

    def delete(self, mid):

        try:
            movie_service.delete(mid)
            return '', 204
        except Exception as e:
            return str(e), 404