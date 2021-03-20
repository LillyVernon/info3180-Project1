from . import db


class Property(db.Model):
     __tablename__ = "property"
     id = db.Column(db.Integer, primary_key=True)
     property_title = db.Column(db.String(80), unique=True)
     description= db.Column(db.String(1000))
     rooms= db.Column(db.Integer)
     bathrooms= db.Column(db.Integer)
     price= db.Column(db.Integer)
     propery_type= db.Column(db.String(1000))
     location= db.Column(db.String(1000))
     photo_name = db.Column(db.String(30), index=True)
     #photo= db.Column(db.LargeBinary(length=2048))

     def __init__(self, property_title,description, rooms, bathrooms, price, property_type, location, photo_name):
        self.property_title = property_title
        self.description = description
        self.rooms=rooms
        self.bathrooms=bathrooms
        self.price=price
        self.propery_type=property_type
        self.location=location
        self.photo_name=photo_name
        #self.photo=photo

     def __repr__(self):
        return '<Property %r>' % self.photo_name