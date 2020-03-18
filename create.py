from application import db
from application.models import Hobby, Location

db.drop_all()
db.create_all()