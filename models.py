from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    animes = db.relationship('Anime', secondary= 'join', backref= 'users')

    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username' : self.username
        }
    

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)

    def __init__(self, name, img):
        self.name = name
        self.img = img

    def save_anime(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'img' : self.img,
        }
    

class Join(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    anime_id = db.Column(db.Integer, db.ForeignKey('anime.id'), nullable=False) 


    def __init__(self, user_id, anime_id):
        self.user_id = user_id
        self.anime_id = anime_id

    # def save_to_list(self):
    #     db.session.add(self)
    #     db.session.commit()

    
        