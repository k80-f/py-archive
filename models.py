# models.py

from app import db
 
 
class Owner(db.Model):
    __tablename__ = "owners"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
 
    def __repr__(self):
        return "<Owner: {}>".format(self.name)
 
 
class Title(db.Model):
    __tablename__ = "titles"
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    subject_matter = db.Column(db.String)
    publisher = db.Column(db.String)
    media_type = db.Column(db.String)
    file_url = db.Column(db.String)
 
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))
    owner = db.relationship("Owner", backref=db.backref(
        "titles", order_by=id), lazy=True)
