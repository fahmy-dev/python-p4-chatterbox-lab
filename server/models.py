from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, func
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    username = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc).astimezone())
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc).astimezone(), onupdate=lambda: datetime.now(timezone.utc).astimezone())

    def __repr__(self):
        return f'<Message {self.id}: {self.body} by {self.username}: {self.created_at}: {self.updated_at}>'