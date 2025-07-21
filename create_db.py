from models import User, Podcast, News
from ext import app, db

with app.app_context():
    db.create_all()
    print("Tables created successfully.")