from flask import Flask, render_template, redirect, request, session, url_for
import socketio
import eventlet
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import json
from urllib.parse import quote, unquote

app = Flask(__name__, template_folder="./public", static_folder="./public/static")
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODOFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=1)
db = SQLAlchemy(app)
sio = socketio.Server()
sioApp = socketio.WSGIApp(sio, app, static_files={
    "/": "./public/"
})




class User(db.Model):
    __tablename__ = "users"
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    rooms = db.relationship("Room", back_populates="users", secondary="users_rooms")
    
        
        
        
class Room(db.Model):
    __tablename__ = "rooms"
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    users = db.relationship("User", back_populates="rooms", secondary="users_rooms")
    
    
    
class users_rooms(db.Model):
    __tablename__ = "users_rooms"
    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("user id", db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    room_id = db.Column("room id", db.Integer, db.ForeignKey("rooms.id", ondelete='CASCADE'))




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        
        found_user = User.query.filter_by(name=user).first()   #najde všechny users co maj to name, first je protože chceš jenom jednoho user
        if found_user == None:
            usr = User(name=user)
            db.session.add(usr)
            db.session.commit()
        else:
            print(f"found user {found_user.name}")
            session["found_userID"] = found_user._id
                    
        print(session["user"])
        return redirect(url_for("chatRooms", user=user))
    else:
        return render_template("login.html")


@app.route("/chatRooms/<user>")
def chatRooms(user):
    print("user: in chatrooms "+user)
    if "found_userID" in session:
        found_userID = session["found_userID"]
        found_roomsUsers = users_rooms.query.filter_by(user_id=found_userID).all()    #vyhodí jenom instance v tý tabulce co to spojuje
        if found_roomsUsers:
            print("rooms:")
            found_rooms = []
            rooms = []
            for roomUser in found_roomsUsers:
                print(roomUser.room_id)
                found_rooms.append(Room.query.filter_by(_id=roomUser.room_id).first())
            for room in found_rooms:
                print(room.name)
                rooms.append(str(room.name))
            print(rooms)
            if rooms:             
                session["rooms"] = rooms
            return render_template("chatRooms.html", user=user, rooms=session["rooms"])
    return render_template("chatRooms.html", user=user)


@app.route("/chat/<roomName>")
def chat(roomName):
    
    return render_template("chat.html")


@app.route("/logout")
def logout():
    with app.app_context():
        session.clear()
    return redirect(url_for("home"))

@sio.event
def message(sid, msg):
    print(msg)
    sio.emit("message", {"user_id": sid, "text":msg})
    
@sio.event
def connect(sid, environ):
    #sio.emit("connect", sid, to=sid)
    print("connected")
    
@sio.event
def disconnect(sid):
    #with app.app_context():
    #    session.clear()
    print("disconnect")
    

@sio.event
def saveUsername(sid, username):
    with sio.session(sid) as sioSession:
        sioSession["username"] = username
        print("saved username: " +sioSession["username"])
    
@sio.event
def createRoom(sid, input):
    with app.app_context():
        with sio.session(sid) as sioSession:
            user = sioSession["username"]
            print(f"user name: {user}")
            found_user = User.query.filter_by(name=user).first()
            print(f"room name: {input}")
            room = Room(name=input, users=[found_user])
            db.session.add(room)
            db.session.commit()
            
@sio.event
def deleteRoom(sid, roomName):
    print(roomName)
    found = False
    with app.app_context():
        with sio.session(sid) as sioSession:
            rooms = Room.query.filter_by(name=roomName).all()
            for room in rooms:           
                print(room.users)
                for user in room.users:
                    print(user.name)
                    if user.name == sioSession["username"]:
                        found = True
                        break
                if found:
                    break
        db.session.delete(room)
        db.session.commit()
        

        
        
    

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), sioApp)
