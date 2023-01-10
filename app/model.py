import sqlalchemy as sa
from app import db


class Page(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title_id = sa.Column(sa.String)
    title = sa.Column(sa.String)
    date = sa.Column(sa.String)
    content = sa.Column(sa.String)
    tags = sa.Column(sa.String)


