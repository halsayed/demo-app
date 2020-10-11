from app import db


class Todo(db.Model):
    """to-do model"""
    # __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    description = db.Column(db.String(200), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.name
