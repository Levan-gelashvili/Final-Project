from ext import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    birthday = db.Column(db.String())
    country = db.Column(db.String())
    role = db.Column(db.String(20), nullable=False, default='user')

class Podcast(db.Model):

    __tablename__ = "podcasts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    video_url = db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    

class News(db.Model):

    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(300), nullable=False)