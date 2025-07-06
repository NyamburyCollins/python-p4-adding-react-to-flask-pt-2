from flask import request, jsonify, make_response
from .models import db, Movie

def register_routes(app):

    @app.route('/movies', methods=['GET', 'POST'])
    def movies():
        if request.method == 'GET':
            movies = Movie.query.all()
            response = make_response(
                jsonify([movie.to_dict() for movie in movies]),
                200
            )
            return response

        elif request.method == 'POST':
            data = request.get_json()
            new_movie = Movie(title=data.get('title'))
            db.session.add(new_movie)
            db.session.commit()

            response = make_response(
                jsonify(new_movie.to_dict()),
                201
            )
            return response

    @app.route('/movies/<int:id>', methods=['PATCH', 'DELETE'])
    def movie_by_id(id):
        movie = Movie.query.filter_by(id=id).first()

        if not movie:
            return make_response({"error": "Movie not found"}, 404)

        if request.method == 'PATCH':
            data = request.get_json()
            for attr in data:
                setattr(movie, attr, data[attr])
            db.session.commit()

            response = make_response(
                jsonify(movie.to_dict()),
                200
            )
            return response

        elif request.method == 'DELETE':
            db.session.delete(movie)
            db.session.commit()

            response = make_response(
                jsonify({'deleted': True}),
                200
            )
            return response
