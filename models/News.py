from main import db

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String(225), unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=True)