from main import db

class ExternalLink(db.Model):
    __tablename__ = 'external_links'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    image = db.Column(db.String(225), unique=False, nullable=True)
    link = db.Column(db.String(225), unique=False, nullable=True)