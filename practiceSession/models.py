from datetime import datetime

from sqlalchemy.orm import backref
from config import db, ma
from sqlalchemy import ForeignKey
from marshmallow import INCLUDE, EXCLUDE, fields


class Avocado(db.Model):
    __tablename__ = 'avocado'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(32))
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer, db.ForeignKey("avotype.typeid"))
    regionid = db.Column(db.Integer, db.ForeignKey("avoregion.regionid"))


class AvoType(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32))
    types = db.relationship('Avocado', backref="type_id")


class Avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(32))
    regions = db.relationship('Avocado', backref="region_id")


class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        # sqla_session = db.session
        load_instance = True
        include_relationships = True
        unknown = EXCLUDE

    avocado = fields.Nested("AvoTypeSchema", default=None)


class AvoTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AvoType
        sqla_session = db.session
        load_instance = True
        include_relationships = True


class AvoRegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avoregion
        sqla_session = db.session
        load_instance = True
        include_relationships = True
