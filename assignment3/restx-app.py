"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template, Flask
from flask_restx import Resource, Api, resource

# local modules
import config
from flask import make_response, abort
from config import db
from models import Avocado, AvocadoSchema


# Get the application instance
# connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
# connex_app.add_api("swagger.yml")
app = Flask(__name__)

api = Api(app)


@api.route('/avocado')
class readall(Resource):
    def get(self):

        people = Avocado.query.order_by(Avocado.id).all()

        person_schema = AvocadoSchema(many=True)
        data = person_schema.dump(people)
        return data


def read_one(id):

    person = Avocado.query.filter(Avocado.id == id).one_or_none()

    if person is not None:

        person_schema = AvocadoSchema()
        data = person_schema.dump(person)
        return data

    else:
        abort(
            404,
            "Person not found for Id: {id}".format(id=id),
        )

# # create a URL route in our application for "/"
# @connex_app.route("/")
# def home():
#     """
#     This function just responds to the browser URL
#     localhost:5000/
#     :return:        the rendered template "home.html"
#     """
#     return render_template("home.html")


if __name__ == "__main__":
    db.init_app(app)
    app.run(host='localhost', port=5000, debug=True)
    #connex_app.run(host='localhost', port=5000, debug=True)
