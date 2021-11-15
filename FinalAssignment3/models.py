from config import db, ma
from marshmallow import fields
from marshmallow import EXCLUDE


class Directors(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    gender = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    department = db.Column(db.String(32))

    movies = db.relationship(
        'Movies',
        backref='directors',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(movies.c.id)'
    )


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.String(32), nullable=False)
    budget = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    release_date = db.Column(db.String(32))
    revenue = db.Column(db.Integer)
    title = db.Column(db.String(32))
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.Integer)
    overview = db.Column(db.String(32))
    tagline = db.Column(db.String(32))
    uid = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))


class DirectorsSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Directors
        sqla_session = db.session
        include_relationships = True
        load_instance = True
        unknown = EXCLUDE

    movies = fields.Nested('DirectorsMoviesSchema', default=[], many=True)


class DirectorsMoviesSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    release_date = fields.Str()
    budget = fields.Int()
    title = fields.Str()
    original_title = fields.Str()


class MovieSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Movies
        sqla_session = db.session
        include_relationships = True
        load_instance = True
        unknown = EXCLUDE

    directors = fields.Nested("MovieDirectorSchema", default=None)


class MovieDirectorSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    uid = fields.Int()
    name = fields.Str()
    gender = fields.Int()
    department = fields.Str()
