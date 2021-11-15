
from flask import make_response, abort
from config import db
from models import Directors, Movies, MovieSchema


def read_all():
    movies = Movies.query.order_by(db.desc(Movies.id)).limit(50)

    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data


def read_one(director_id, movie_id):
    movie = (
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        .filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data

    else:
        abort(404, f"movie not found for Id: {movie_id}")


def create(director_id, movies):
    directors = Directors.query.filter(
        Directors.id == director_id).one_or_none()

    if directors is None:
        abort(404, f"director not found for Id: {director_id}")

    schema = MovieSchema()
    new_movie = schema.load(movies, session=db.session)

    directors.movies.append(new_movie)
    db.session.commit()

    data = schema.dump(new_movie)

    return data, 201


def update(director_id, movie_id, movies):
    update_movies = (
        Movies.query.filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    if update_movies is not None:

        schema = MovieSchema()
        update = schema.load(movies, session=db.session)

        update.director_id = update_movies.director_id
        update.id = update_movies.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_movies)

        return data, 200

    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def delete(director_id, movie_id):
    movies = (
        Movies.query.filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )
    if movies is not None:
        db.session.delete(movies)
        db.session.commit()
        return make_response(
            "movies {movie_id} deleted".format(movie_id=movie_id), 200
        )

    else:
        abort(404, f"Movie not found for Id: {movie_id}")
