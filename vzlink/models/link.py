from vzlink import db
from datetime import datetime


class Link(db.Model):
    __tablename__ = 'link'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        index=True
    )

    long_link = db.Column(
        db.String(1000)
    )

    hash_id = db.Column(
        db.String(10)
    )
    
    created_on = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    last_used = db.Column(
        db.DateTime,
        default=None
    )

    times_used = db.Column(
        db.Integer,
        default=0
    )

    link_owner = db.relationship(
        'User',
        backref='link',
        foreign_keys=[user_id]
    )

    def __init__(
        self,
        user_id,
        long_link
    ):

        self.user_id = user_id
        self.long_link = long_link

    def commit_link(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
