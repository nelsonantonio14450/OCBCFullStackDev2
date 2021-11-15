
from flask import make_response, abort
from sqlalchemy.orm import session
from config import db
from models import Avocado, AvocadoSchema, Avoregion, AvoType


def read_all():

    avocado = Avocado.query.order_by(Avocado.id).all()
    # avocado = (
    #     Avocado.query
    #     .join(AvoType)
    #     .all()
    # )
    # avocado = (
    #     session.query(Avocado, Avoregion, AvoType).
    #     filter(
    #         Avocado.regionid == Avoregion.regionid).
    #     filter(Avocado.type == AvoType.typeid).all()
    # )
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocado)
    return data


def read_one(id):

    avocado = Avocado.query.filter(Avocado.id == id).one_or_none()

    if avocado is not None:

        avocado_schema = AvocadoSchema()
        data = avocado_schema.dump(avocado)
        return data

    else:
        abort(
            404,
            "avocado not found for Id: {id}".format(id=id),
        )


def create(avocado):

    schema = AvocadoSchema()
    new_avo = schema.load(avocado, session=db.session)
# validasi fk
    avotype = AvoType.query.filter(
        AvoType.typeid == avocado['type']
    ).one_or_none()

    regid = Avoregion.query.filter(
        Avoregion.regionid == avocado['regionid']
    ).one_or_none()

    if avotype is None:
        abort(
            404,
            "avotype not found"
        )
    elif regid is None:
        abort(
            404,
            "region not found"
        )
    else:

        db.session.add(new_avo)
        db.session.commit()

        data = schema.dump(new_avo)

        return data, 201


def update(id, avocado):

    update_avocado = Avocado.query.filter(
        Avocado.id == id
    ).one_or_none()

    schema = AvocadoSchema()
    update = schema.load(avocado, session=db.session)

    if update_avocado is None:
        abort(
            404,
            "avocado not found for Id: {id}".format(id=id),
        )

    avotype = AvoType.query.filter(
        AvoType.typeid == avocado['type']
    ).one_or_none()

    regid = Avoregion.query.filter(
        Avoregion.regionid == avocado['regionid']
    ).one_or_none()

    if avotype is None:
        abort(
            404,
            "avotype not found"
        )
    elif regid is None:
        abort(
            404,
            "region not found"
        )
    else:

        update.id = update_avocado.id
        db.session.merge(update)
        db.session.commit()
        data = schema.dump(update_avocado)

        return data, 200


def delete(id):

    avocado = Avocado.query.filter(Avocado.id == id).one_or_none()

    # Did we find a person?
    if avocado is not None:
        db.session.delete(avocado)
        db.session.commit()
        return make_response(
            "Person {id} deleted".format(id=id), 200
        )
    else:
        abort(
            404,
            "avocado not found for Id: {id}".format(id=id),
        )
