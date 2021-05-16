import random
import string
from datetime import date
from App import db


class enterURL(db.Model):
    urlId = db.Column(db.Integer, primary_key=True)
    longURL= db.Column(db.String(200), index=True, unique=False)
    shortURL = db.Column(db.String(10), index=False, unique=True)
    createdAt = db.Column(db.Date, default=date.today())   

    def __repr__(self):
        return '<URLshort {} : URLlong {} >'.format(self.shortURL, self.longURL)
