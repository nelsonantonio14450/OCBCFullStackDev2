
from flask import make_response, abort
from config import db
from models import Directors, Movies, DirectorsSchema


def read_all():
    """
    fungsi Read all, untuk fetch semua data dengan limit 100 agar tidak lama 
    dalam fetching data dari database, return berisi list directors dan movie yang pernah di directnya
    return dalam bentuk list/json
    """
    directors = Directors.query.order_by(Directors.id).limit(100)

    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)
    return data


def read_one(director_id):
    """
    fungsi Read one, untuk fetch 1 data, menerima parameter director_id, dengan 
     return berisi list director dan list movies yang pernah di directnya
    return dalam bentuk list/json
    """
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


def get_by_department(department):
    """
    fungsi sorting by department dari directors, fungsi ini untuk search siapa saja yang terdapat 
    pada department dari parameter input, menerima parameter department, return list/json dari directors 
    yang sesuai kriteria
    """
    directors = (Directors.query.filter(
        Directors.department.like(department)).limit(100))

    if directors is not None:
        director_schema = DirectorsSchema(many=True)
        data = director_schema.dump(directors)
        return data

    else:
        abort(404, f"director not found for department: {department}")


def get_by_gender(gender):
    """
    fungsi sorting by gender dari directors, fungsi ini untuk search siapa saja yang terdapat 
    pada gender dari parameter input, menerima parameter gender, return list/json dari directors 
    yang sesuai kriteria
    """
    directors = (Directors.query.with_entities(Directors.uid, Directors.name, Directors.department).filter(
        Directors.gender == gender).limit(100))

    if directors is not None:
        director_schema = DirectorsSchema(many=True)
        data = director_schema.dump(directors)
        return data

    else:
        abort(404, f"director not found for gender: {gender}")


def get_by_name(name):
    """
    fungsi search directors by name, menerima parameter nama untuk mencari nama dari directors yang sesuai
    dengan inputan, return json/list dari directors dan movies yang sesuai kriteria
    """
    search = "%{}%".format(name)

    directors = (Directors.query.filter(
        Directors.name.like(search)).limit(100))

    if directors is not None:
        director_schema = DirectorsSchema(many=True)
        data = director_schema.dump(directors)
        return data

    else:
        abort(404, f"director not found for name: {name}")


def create(directors):
    """
    fungsi untuk menginsert directors, menerima parameter list directors untuk diinput kedalam database, 
    return dengan kode 200 jika berhasil
    """
    schema = DirectorsSchema()
    new_dire = schema.load(directors, session=db.session)

    db.session.add(new_dire)
    db.session.commit()

    data = schema.dump(new_dire)

    return data, 201


def update(director_id, directors):
    """
    fungsi untuk update directors, menerima parameter director_id dan list directors untuk 
    diupdate kedalam database dengan ketentuan id dari director sesuai dengan parameter director_id, 
    return dengan kode 200 jika berhasil, jika tidak ditemukan director_id pada database akan 
    memunculkan kode error 404 not found
    """
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
    """
    fungsi menghapus directors dan movies yang pernah dibuatnya dari database, menerima parameter 
    director_id, penghapusan didasarkan pada inputan, return 200 jika berhasil, jika tidak
    ada director_id yang sesuai dengan input maka 404 not found
    """
    dire = Directors.query.filter(
        Directors.id == director_id).one_or_none()  # directors

    if dire is not None:
        db.session.delete(dire)
        db.session.commit()
        return make_response(f"director {director_id} deleted", 200)

    else:
        abort(404, f"direcor not found for Id: {director_id}")
