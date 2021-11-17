from config import db, ma
from marshmallow import fields
from marshmallow import EXCLUDE


class Directors(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text)
    gender = db.Column(db.BigInteger)
    uid = db.Column(db.BigInteger)
    department = db.Column(db.Text)

    movies = db.relationship(
        'Movies',
        backref='directors',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(movies.c.id)'
    )


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.BigInteger, primary_key=True)
    original_title = db.Column(db.Text, nullable=False)
    budget = db.Column(db.BigInteger)
    popularity = db.Column(db.BigInteger)
    release_date = db.Column(db.Text)
    revenue = db.Column(db.BigInteger)
    title = db.Column(db.Text)
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.BigInteger)
    overview = db.Column(db.Text)
    tagline = db.Column(db.Text)
    uid = db.Column(db.BigInteger)
    director_id = db.Column(db.BigInteger, db.ForeignKey("directors.id"))


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
