from flask import Flask, render_template, redirect, request, session, url_for, jsonify, flash
import socketio
import eventlet
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import json
from urllib.parse import quote, unquote
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__, template_folder="./public", static_folder="./public/static")
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatApp.db"
app.config["SQLALCHEMY_TRACK_MODOFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=1)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
db = SQLAlchemy(app)
sio = socketio.Server()
sioApp = socketio.WSGIApp(sio, app, static_files={
    "/": "./public/"
})




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




def getRoomId(userRooms, roomName):
    print(userRooms)
    print(roomName)
    for userRoom in userRooms:
        if (userRoom.name == roomName):
            return userRoom.id
        
        




@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("chatRooms", user=session["user"]))
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        
        found_user = User.query.filter_by(name=user).first()   #najde všechny users co maj to name, first je protože chceš jenom jednoho user
        if found_user == None:
            flash("Uživatel s tímto uživatelským jménem neexistuje")
            return redirect(url_for("login"))
        elif (not found_user.check_password(request.form["password"])):
            flash("Zadal jste špatné heslo", "danger")
            return redirect(url_for("login"))
        else:
            print(f"found user {found_user.name}")
            session["found_userID"] = found_user.id
                    
        print("Entered username saved in session as user: "+session["user"])
        return redirect(url_for("chatRooms", user=user))
    else:
        return render_template("login.html")
    
@app.route("/register", methods=["POST", "GET"])
def register():
    with app.app_context():
        if (request.method == "POST"):
            if (User.query.filter_by(name=request.form["nm"]).first()):
                flash("Toto uživatelské jméno je již zabrané", "danger")
                return redirect(url_for("register"))
            if (request.form["password"] != request.form["passwordCheck"]):
                flash("Vámi zadaná hesla se musí shodovat!", "danger")
                return redirect(url_for("register"))
            user = User(name=request.form["nm"], password=generate_password_hash(request.form["password"]))
            session["user"] = user.name
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("chatRooms", user=user.name))
    return render_template("register.html")


@app.route("/chatRooms/<user>")
def chatRooms(user):
    print("user: in chatrooms "+user)
    if "found_userID" in session:   #pokud v session je záznam o found_userID
        found_userID = session["found_userID"]
        userAccount = User.query.filter_by(name=user).first()
        if (userAccount.id != found_userID):
            found_userID = userAccount.id
            print("id se nerovnalo, id je změněno")
        print("found_userID: "+str(found_userID))    #zkus na debug
        found_roomsUsers = users_rooms.query.filter_by(user_id=found_userID).all()    #vyhodí jenom instance v tý tabulce co to spojuje
        if found_roomsUsers:
            print("rooms:")
            found_rooms = []
            rooms = []
            for roomUser in found_roomsUsers:
                print(roomUser.room_id)
                found_rooms.append(Room.query.filter_by(id=roomUser.room_id).first())
            #for room in found_rooms:
            #    print(room.name)
            #    rooms.append(str(room.name))
            print(f"found rooms: {found_rooms}")
            #if found_rooms:             
                #session["found_rooms"] = found_rooms
            return render_template("chatRooms.html", user=userAccount, rooms=found_rooms)
    return render_template("chatRooms.html", user=user)


@app.route("/chat/<roomId>/<userName>")
def chat(roomId, userName):
    user = User.query.filter_by(name=userName).first()
    print(f"found user {user.name}")
    print(f"found user {user.id}")
    userRooms = [room for room in user.rooms]   #nevim na co to tu je
    room = Room.query.filter_by(id=roomId).first()
    usersInRoom = [userInRoom for userInRoom in room.users]
    
    
    for userInRoom in usersInRoom:  #tady je userInRoom místo user protože to jinak přepsalo toho user co jsem deklaroval na začátku def chat, pak byl user uloženej poslední user přidanej v roomce
        print(f"user in this chat: {userInRoom.name}")
        print(f"user id in this chat: {userInRoom.id}")
    #print(f"current userId: {user.id}")
        
    print("Name of room that you are in: "+room.name)
    print("ID of room that you are in: "+str(room.id))
    messages = [message for message in room.messages]   #narve do jedný proměný všechny messages objekty z týhle room
    
    #DEBUG
    #print("Raw messages:")
    #for m in messages:
    #    print(f"ID: {m.id}, Text: {m.content}, User ID: {m.user_id}, User Name: {m.user.name}, pico: {m.user_id==user.id}")
    #    print(user.id)

    
    messages_with_owner_flag = [    #předělá messages do něčeho čitelnějšího aby se z toho daly líp brát ty data do html
        {
            "id": m.id,
            "text": m.content,
            "user_id": m.user_id,
            "user_name": m.user.name,
            "is_current_user": m.user_id == user.id,    #pokud true, tak se zpráva obarví na modro, aby šlo poznat že to je zpráva usera co na to kouká
        }
        for m in messages
    ]
    
    print("MSGS: ")
    print(messages_with_owner_flag)
    if (len(messages) == 0):
        return render_template("chat.html", users=usersInRoom)
    return render_template("chat.html", users=usersInRoom, messages=messages_with_owner_flag)


@app.route("/logout")
def logout():
    with app.app_context():
        session.clear()
    return redirect(url_for("home"))


@sio.event
def saveUsername(sid, username):    #funkce co uloží do sio session username
    with sio.session(sid) as sioSession:
        sioSession["username"] = username
        print("saved username: " +sioSession["username"])
        
@sio.event
def saveRoomname(sid, roomname):
    with sio.session(sid) as sioSession:
        sioSession["roomname"] = roomname
        print("saved roomname: " +sioSession["roomname"])
        
@sio.event
def saveRoomId(sid, roomId):
    with sio.session(sid) as sioSession:
        sioSession["roomId"] = roomId
        print("saved roomId: " +sioSession["roomId"])
        sio.enter_room(sid, sioSession["roomId"])
        print(f"sio rooms tohoto usera: {sio.rooms(sid)}")

@sio.event
def message(sid, msg):
    print("message: "+msg)
    with app.app_context():
        with sio.session(sid) as sioSession:
            message = Message(content=msg)
            user = sioSession["username"]
            user = User.query.filter_by(name=user).first()
            print("user name: "+user.name)
            userRooms = [room for room in user.rooms]
            room = Room.query.filter_by(id=sioSession["roomId"]).first()
            room.messages.append(message)
            user.messages.append(message)
            db.session.add(message)
            db.session.commit()
        
    sio.emit("message", {"user_id": sid, "text":msg, "username":sioSession["username"]}, to=sioSession["roomId"])  #je tam to, protože jinak to posílalo msgs všem a ne tý roomce kde se napsala
    
@sio.event
def addUser(sid, userToAddName):
    print("user to add: "+userToAddName)
    with app.app_context():
        userToAdd = User.query.filter_by(name=userToAddName).first()
        if (userToAdd):
            print("USER NALEZEN")
            with sio.session(sid) as sioSession:
                mainUser = User.query.filter_by(name=sioSession["username"]).first()
                room = Room.query.filter_by(id=sioSession["roomId"]).first()
                room.users.append(userToAdd)
                db.session.commit()
        else:
            print("USER NENALEZEN")
    
@sio.event
def connect(sid, environ):  #sid je stejný jak v pythonu tak v js
    #sio.emit("connect", sid, to=sid)
    #sio.enter_room(sid, "a")   sio roomka je id té roomky
    print("connected")
    
@sio.event
def disconnect(sid):
    #with app.app_context():
    #    session.clear()
    print("disconnect")
    
@sio.event
def createRoom(sid, input):
    with app.app_context():
        with sio.session(sid) as sioSession:
            user = sioSession["username"]
            print(f"user name: {user}")
            found_user = User.query.filter_by(name=user).first()
            print(f"room name: {input}")
            room = Room(name=input, users=[found_user], owner_id=found_user.id)
            db.session.add(room)
            db.session.commit()
            print(sio.rooms(sid))
            print(f"roomka pico: {room.name}")
            sio.emit("createRoom", {"roomName": input, "roomId": room.id}, to=sid)
            
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
        
@sio.event
def leaveRoom(sid, roomId):
    print(roomId)
    with app.app_context():
        with sio.session(sid) as sioSession:
            user = User.query.filter_by(name=sioSession["username"]).first()
        print(user.name)  
        db.session.query(users_rooms).filter_by(user_id=user.id, room_id=roomId).delete()
        db.session.commit()  
        

        
        
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), sioApp)
