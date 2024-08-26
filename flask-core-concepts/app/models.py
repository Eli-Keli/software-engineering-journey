from . import db

# Define Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"