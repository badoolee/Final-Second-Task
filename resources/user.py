from flask_smorest import Blueprint, abort
from flask.views import MethodView

from db import db
from models.user import UserModel
from schemas import UserSchema, UserUpdateSchema

Userblp = Blueprint("user", __name__)

@Userblp.route("/api/<int:user_id>")
class User_Op(MethodView):
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            return user.json()
        
        return {"Message":"Wrong ID Number"}
    
    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"Message": "The User details is deleted Successfully"}, 200
        
        return {"Message":"Wrong ID Number"}
        
    
    @Userblp.arguments(UserUpdateSchema)
    def put(self, user_data, user_id: int):
        user = UserModel.query.get(user_id)
        if user:
            user.occupation = user_data["occupation"]
            user.location = user_data["location"]
        else:
            return {"Message":"Wrong ID Number"}

        db.session.add(user)
        db.session.commit()

        return user.json()
    

@Userblp.route("/api")
class User(MethodView):
    @Userblp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter_by(name=user_data["name"]).first():
            return{"Message": "A User With That Name Already Exists, Use Another Name"}
        
        user = UserModel(name=user_data["name"],
                         occupation=user_data["occupation"],
                         location=user_data["location"])
        db.session.add(user)
        db.session.commit()

        return user.json()
    

