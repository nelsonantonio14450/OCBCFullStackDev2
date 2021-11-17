
from flask import make_response, abort
from config import db
from models import Directors, Movies, MovieSchema
import datetime


def read_all():
    """
    fungsi Read all, untuk fetch semua data dengan limit 100 agar tidak lama 
    dalam fetching data dari database, return berisi list movie dan directorsnya
    """
    movies = Movies.query.order_by(db.desc(Movies.id)).limit(100)

    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data


def read_one(director_id, movie_id):
    """
    fungsi Read one, untuk fetch 1 data dengan ketentuan parameter director_id dan movie_id, 
    return berisi movie dan directornya
    """
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
    """
    fungsi sorting by more budget, fetch semua data yang budgetnya lebih dari parameter, 
    menerima parameter budget sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.budget >= budget).order_by(Movies.budget).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this budget : {budget}")


def get_by_LessBudget(budget):
    """
    fungsi sorting by less budget, fetch semua data yang budgetnya kurang dari parameter, 
    menerima parameter budget sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.budget <= budget).order_by(Movies.budget.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this budget : {budget}")


def get_by_BetweenBudget(budget1, budget2):
    """
    fungsi sorting by between budget, fetch semua data yang budgetnya diantara dari 2 parameter, 
    menerima 2 parameter budget sebagai input, return movie dan directors yang sesuai kriteria
    """
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
    """
    fungsi sorting by more revenue, fetch semua data yang revenuenya lebih dari parameter, 
    menerima parameter revenue sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.revenue >= revenue).order_by(Movies.revenue).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this revenue : {revenue}")


def get_by_LessRev(revenue):
    """
    fungsi sorting by less revenue, fetch semua data yang revenuenya kurang dari parameter, 
    menerima parameter revenue sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.revenue <= revenue).order_by(Movies.revenue.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this revenue : {revenue}")


def get_by_BetweenRev(rev1, rev2):
    """
    fungsi sorting by between revenue, fetch semua data yang revenuenya diantara dari 2 parameter, 
    menerima 2 parameter revenue sebagai input, return movie dan directors yang sesuai kriteria
    """
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
    """
    fungsi sorting by more popular, fetch semua data yang popularity lebih dari parameter, 
    menerima parameter popularity sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.popularity >= pop).order_by(Movies.popularity).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this popularity : {pop}")


def get_by_LessPopularity(pop):
    """
    fungsi sorting by less popular, fetch semua data yang popularity kurang dari parameter, 
    menerima parameter popularity sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.popularity <= pop).order_by(Movies.popularity.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this popularity : {pop}")


def get_by_BetweenPopularity(pop1, pop2):
    """
    fungsi sorting by between popularity, fetch semua data yang popularity diantara dari 2 parameter, 
    menerima 2 parameter popularity sebagai input, return movie dan directors yang sesuai kriteria
    """
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
    """
    fungsi sorting by more vote_count, fetch semua data yang vote_count lebih dari parameter, 
    menerima parameter vote_count sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.vote_count >= vote).order_by(Movies.vote_count).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this vote : {vote}")


def get_by_Lessvote(vote):
    """
    fungsi sorting by less vote_count, fetch semua data yang vote_count kurang dari parameter, 
    menerima parameter vote_count sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.vote_count <= vote).order_by(Movies.vote_count.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this vote : {vote}")


def get_by_Betweenvote(vote1, vote2):
    """
    fungsi sorting by between vote_count, fetch semua data yang vote_count diantara dari 2 parameter, 
    menerima 2 parameter vote_count sebagai input, return movie dan directors yang sesuai kriteria
    """
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
    """
    fungsi sorting by more vote_average, fetch semua data yang vote_average lebih dari parameter, 
    menerima parameter vote_average sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.vote_average >= vote).order_by(Movies.vote_average).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this vote avg: {vote}")


def get_by_Lessvoteavg(vote):
    """
    fungsi sorting by less vote_average, fetch semua data yang vote_average kurang dari parameter, 
    menerima parameter vote_average sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.vote_average <= vote).order_by(Movies.vote_average.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this vote avg : {vote}")


def get_by_Betweenvoteavg(vote1, vote2):
    """
    fungsi sorting by between vote_average, fetch semua data yang vote_average diantara dari 2 parameter, 
    menerima 2 parameter vote_average sebagai input, return movie dan directors yang sesuai kriteria
    """
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
    """search by title, mencari title berdasarkan hasil inputan, menggunakan syntax like 
    dimana nanti akan mencari title yang mirip pada depan dan belakangnya (%:input:%)"""

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
    """
    fungsi sorting by more release_date, fetch semua data yang release_date lebih dari parameter, 
    menerima parameter release_date sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.release_date >= date).order_by(Movies.release_date).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this date : {date}")


def get_by_Lessdate(date):
    """
    fungsi sorting by less release_date, fetch semua data yang release_date kurang dari parameter, 
    menerima parameter release_date sebagai input, return movie dan directors yang sesuai kriteria
    """
    movie = (Movies.query.filter(
        Movies.release_date <= date).order_by(Movies.release_date.desc()).limit(100))

    if movie is not None:
        director_schema = MovieSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are less than this revenue : {date}")


def get_by_Betweendate(date1, date2):
    """
    fungsi sorting by between release_date, fetch semua data yang release_date diantara dari 2 parameter, 
    menerima 2 parameter release_date sebagai input, return movie dan directors yang sesuai kriteria
    """
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
    """
    fungsi insert untuk memasukan movie berdasarkan directornya, menerima 2 parameter yaitu director_id
    dan movies yang berupa dict/json, return data yang diinput dan response code 201,
    jika gagal seperti salah director_id dan input tanggal tidak sesuai maka tidak akan terinsert
    """
    directors = Directors.query.filter(
        Directors.id == director_id).one_or_none()

    if directors is None:
        abort(404, f"director not found for Id: {director_id}")

    try:  # validate input date
        inputDate = movies['release_date']
        year, month, day = inputDate.split('-')
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        abort(400, f"not valid date: {inputDate}")

    schema = MovieSchema()
    new_movie = schema.load(movies, session=db.session)

    directors.movies.append(new_movie)
    db.session.commit()

    data = schema.dump(new_movie)

    return data, 201


def update(director_id, movie_id, movies):
    """
    fungsi update untuk memperbaharui movie berdasarkan directornya, menerima 3 parameter yaitu director_id,
    movie_id dan movies yang berupa dict/json, return data yang diinput dan response code 200 jika berhasil,
    jika gagal seperti salah movie_id/director_id dan input tanggal tidak sesuai maka tidak akan terupdate
    """
    update_movies = (
        Movies.query.filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    try:  # validate input date
        inputDate = movies['release_date']
        year, month, day = inputDate.split('-')
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        abort(400, f"not valid date: {inputDate}")

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
    """
    fungsi ini untuk menghapus movie berdasarkan movie_id dan director_id, menerima 2 parameter tersebut,
    dan jika berhasil mengembalikan response code 200, jika gagal karena tidak ada id ditemukan maka return
    404 not found
    """
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
