from app import db
from models import User, Post

db.create_all()

db.session.commit()