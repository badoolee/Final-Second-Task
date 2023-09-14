from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    occupation = fields.Str(required=True)
    location = fields.Str(required=True)

class UserUpdateSchema(Schema):
    occupation = fields.Str()
    location = fields.Str()
