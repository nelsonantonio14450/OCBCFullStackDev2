
from flask import make_response, abort
from config import db
from models import Directors, Movies, MovieSchema


def read_all():
    movies = Movies.query.order_by(db.desc(Movies.id)).limit(100)

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


def get_by_MoreBudget(budget):
    movie = (Movies.query.filter(
        Movies.budget >= budget).order_by(Movies.budget).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this budget : {budget}")


def get_by_LessBudget(budget):
    movie = (Movies.query.filter(
        Movies.budget <= budget).order_by(Movies.budget.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this budget : {budget}")


def get_by_BetweenBudget(budget1, budget2):
    movie = (Movies.query.filter(
        Movies.budget >= budget1).filter(Movies.budget <= budget2).order_by(Movies.budget).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(
            404, f"no data that are between this budget : {budget1}, {budget2}")

# revenue


def get_by_MoreRev(revenue):
    movie = (Movies.query.filter(
        Movies.revenue >= revenue).order_by(Movies.revenue).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this revenue : {revenue}")


def get_by_LessRev(revenue):
    movie = (Movies.query.filter(
        Movies.revenue <= revenue).order_by(Movies.revenue.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this revenue : {revenue}")


def get_by_BetweenRev(rev1, rev2):
    movie = (Movies.query.filter(
        Movies.revenue >= rev1).filter(Movies.revenue <= rev2).order_by(Movies.revenue).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(
            404, f"no data that are between this revenue : {rev1}, {rev2}")

# popularity


def get_by_MorePopularity(pop):
    movie = (Movies.query.filter(
        Movies.popularity >= pop).order_by(Movies.popularity).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this popularity : {pop}")


def get_by_LessPopularity(pop):
    movie = (Movies.query.filter(
        Movies.popularity <= pop).order_by(Movies.popularity.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this popularity : {pop}")


def get_by_BetweenPopularity(pop1, pop2):
    movie = (Movies.query.filter(
        Movies.popularity >= pop1).filter(Movies.popularity <= pop2).order_by(Movies.popularity).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(
            404, f"no data that are between this popularity : {pop1}, {pop2}")

# vote count


def get_by_Morevote(vote):
    movie = (Movies.query.filter(
        Movies.vote_count >= vote).order_by(Movies.vote_count).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this vote : {vote}")


def get_by_Lessvote(vote):
    movie = (Movies.query.filter(
        Movies.vote_count <= vote).order_by(Movies.vote_count.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this vote : {vote}")


def get_by_Betweenvote(vote1, vote2):
    movie = (Movies.query.filter(
        Movies.vote_count >= vote1).filter(Movies.vote_count <= vote2).order_by(Movies.vote_count).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(
            404, f"no data that are between this vote : {vote1}, {vote2}")

# vote average


def get_by_Morevoteavg(vote):
    movie = (Movies.query.filter(
        Movies.vote_average >= vote).order_by(Movies.vote_average).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this vote avg: {vote}")


def get_by_Lessvoteavg(vote):
    movie = (Movies.query.filter(
        Movies.vote_average <= vote).order_by(Movies.vote_average.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this vote avg : {vote}")


def get_by_Betweenvoteavg(vote1, vote2):
    movie = (Movies.query.filter(
        Movies.vote_average >= vote1).filter(Movies.vote_average <= vote2).order_by(Movies.vote_average).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(
            404, f"no data that are between this vote avg : {vote1}, {vote2}")


def get_by_title(title):
    search = "%{}%".format(title)

    movies = (Movies.query.filter(
        Movies.title.like(search)).limit(100))

    if movies is not None:
        movie_schema = MovieSchema(many=True)
        data = movie_schema.dump(movies)
        return data

    else:
        abort(404, f"director not found for name: {title}")


# date release

def get_by_Moredate(date):
    movie = (Movies.query.filter(
        Movies.release_date >= date).order_by(Movies.release_date).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this date : {date}")


def get_by_Lessdate(date):
    movie = (Movies.query.filter(
        Movies.release_date <= date).order_by(Movies.release_date.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this revenue : {date}")


def get_by_Betweendate(date1, date2):
    movie = (Movies.query.filter(
        Movies.release_date >= date1).filter(Movies.release_date <= date2).order_by(Movies.release_date).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(
            404, f"no data that are between this revenue : {date1}, {date2}")


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
