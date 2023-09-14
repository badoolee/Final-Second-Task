import os
from flask import Flask
from flask_smorest import Api


from db import db
from resources.user import Userblp


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Student Administration"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["SQLALCHEMY_DATABASE_URI"] =  os.getenv("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


api = Api(app)

@app.before_request
def create_tables():
    db.create_all()

api.register_blueprint(Userblp)

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)