from app import db

class Blogpost(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    subtitle = db.Column(db.String(64))
    author = db.Column(db.String(64))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)



    # def __repr__(self):
    #     return f'<Book: {self.title}>'
