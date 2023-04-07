import datetime as datetime
import sqlalchemy as sql
import database as database

class Recipe(database.Base):
    __tablename__ = "recipes"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    title = sql.Column(sql.String, index=True)
    ingredients_id = sql.Column(sql.Integer, index=True)
    url = sql.Column(sql.String, index=True, unique=True)
    date_added = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)
    date_updated = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)
