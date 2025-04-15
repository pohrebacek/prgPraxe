from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    password = db.Column(db.String(256), nullable=False)
    rooms = db.relationship("Room", back_populates="users", secondary="users_rooms")
    messages = db.relationship("Message", back_populates="user", cascade="all, delete-orphan")
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
        
        
        
class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    users = db.relationship("User", back_populates="rooms", secondary="users_rooms")
    messages = db.relationship("Message", back_populates="room", cascade="all, delete-orphan")
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    
class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column("id", db.Integer, primary_key=True)
    content = db.Column("content", db.String())
    user = db.relationship("User", back_populates="messages")
    room = db.relationship("Room", back_populates="messages")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    
    
    
    
class users_rooms(db.Model):
    __tablename__ = "users_rooms"
    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("user id", db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    room_id = db.Column("room id", db.Integer, db.ForeignKey("rooms.id", ondelete='CASCADE'))