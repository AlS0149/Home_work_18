from flask_restx import Namespace, Resource
from dao.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):

        result = director_service.get_all()
        if result:
            return directors_schema.dump(result), 200
        else:
            return "Данные не найдены", 404


@director_ns.route('/<int:did>')  # Представление по маршруту /directors/did
class DirectorView(Resource):

    def get(self, did):

        result = director_service.get_one(did)
        if result:
            return director_schema.dump(result), 200
        else:
            return "Данные не найдены", 404