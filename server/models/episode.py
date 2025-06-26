from server import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, unique=True, nullable=False)
    
    appearances = db.relationship('Appearance', backref='episode', cascade='all,delete')