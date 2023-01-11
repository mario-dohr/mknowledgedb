import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Page(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title_id = sa.Column(sa.String)
    title = sa.Column(sa.String)
    date = sa.Column(sa.String)
    content = sa.Column(sa.String)
    tags = sa.Column(sa.String)


