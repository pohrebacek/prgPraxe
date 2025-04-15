from .models import Message, User, Room, users_rooms
from flask import current_app
from . import db
from werkzeug.security import generate_password_hash


def register_socket_events(sio, app):
    @sio.event
    def saveUsername(sid, username):    #funkce co uloží do sio session username
        with sio.session(sid) as sioSession:
            sioSession["username"] = username
            print("saved username: " +sioSession["username"])
            sio.enter_room(sid, username)
            print(f"sioRooms of this user: {sio.rooms(sid)}")

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
                    room = Room.query.filter_by(id=sioSession["roomId"]).first()
                    room.users.append(userToAdd)
                    db.session.commit()
                    sio.emit("showAddedUser", {"userName": userToAddName}, to=sioSession["roomId"])
                    sio.emit("createRoom", {"roomName": room.name, "roomId": room.id, "isAdded": True}, to=userToAddName)
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
    def deleteRoom(sid, roomId):
        print(roomId)
        with app.app_context():
            with sio.session(sid) as sioSession:
                room = Room.query.filter_by(id=roomId).first()
                for user in room.users:
                    if (user.id != room.owner_id):
                        sio.emit("redirectToTheMenu", {"userName": user.name}, to=user.name)
                        sio.emit("deleteRoomFromMenu", {"roomId": room.id}, to=user.name)
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
            sio.emit("showUserThatLeft", {"userName": user.name}, to=roomId); 

    @sio.event
    def kickUser(sid, userToKick):
        print(f"user to kick: {userToKick}")
        with app.app_context():
            with sio.session(sid) as sioSession:
                room = Room.query.filter_by(id=sioSession["roomId"]).first()
                user = User.query.filter_by(name=userToKick).first()
            print(f"roomname: {room.name}")
            print(f"user to kick 2: {user.name}")
            db.session.query(users_rooms).filter_by(user_id=user.id, room_id=room.id).delete()
            db.session.commit()

    @sio.event
    def checkRegisterUserName(sid, formValues):
        print(f"written username: {formValues[0]}")
        with app.app_context():
            if (User.query.filter_by(name=formValues[0]).first()):
                sio.emit("sameUserNameError")
            else:
                user = User(name=formValues[0], password=generate_password_hash(formValues[1]))
                #session["user"] = user.name
                db.session.add(user)
                db.session.commit()
                sio.emit("redirectToMenu", {"username": user.name})

    @sio.event
    def checkLogin(sid, formValues):
        print(f"written username: {formValues[0]}")
        with app.app_context():
            user = User.query.filter_by(name=formValues[0]).first()
            if (not user or not user.check_password(formValues[1])):
                sio.emit("wrongLoginError")
            else:
                sio.emit("redirectToMenu", {"username": user.name})