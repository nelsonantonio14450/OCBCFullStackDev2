
from flask import make_response, abort
from config import db
from models import Directors, Movies, DirectorsSchema


def read_all():
    directors = Directors.query.order_by(Directors.id).limit(50)

    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)
    return data


def read_one(director_id):
    directors = (
        Directors.query.filter(Directors.id == director_id)
        .outerjoin(Movies)
        .one_or_none()
    )

    if directors is not None:

        director_schema = DirectorsSchema()
        data = director_schema.dump(directors)
        return data

    else:
        abort(404, f"director not found for Id: {director_id}")


def create(directors):
    schema = DirectorsSchema()
    new_dire = schema.load(directors, session=db.session)

    db.session.add(new_dire)
    db.session.commit()

    data = schema.dump(new_dire)

    return data, 201


def update(director_id, directors):

    upd_dire = Directors.query.filter(
        Directors.id == director_id
    ).one_or_none()

    if upd_dire is not None:

        schema = DirectorsSchema()
        update = schema.load(directors, session=db.session)

        update.id = upd_dire.id
        db.session.merge(update)
        db.session.commit()
        data = schema.dump(upd_dire)

        return data, 200

    else:
        abort(404, f"director not found for Id: {director_id}")


def delete(director_id):
    dire = Directors.query.filter(
        Directors.id == director_id).one_or_none()  # directors

    if dire is not None:
        db.session.delete(dire)
        db.session.commit()
        return make_response(f"director {director_id} deleted", 200)

    else:
        abort(404, f"direcor not found for Id: {director_id}")
