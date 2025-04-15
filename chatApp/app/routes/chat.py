from flask import Blueprint, render_template, redirect, session, url_for
from .. models import User, Room, users_rooms

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chatRooms/<user>")
def chatRooms(user):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    session["user"] = user
    print("user: in chatrooms "+user)
    if "found_userID" in session:   #pokud v session je záznam o found_userID
        found_userID = session["found_userID"]
        userAccount = User.query.filter_by(name=user).first()
        if (userAccount.id != found_userID):
            return redirect(url_for("auth.login"))
        #    found_userID = userAccount.id
        #    print("id se nerovnalo, id je změněno")
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


@chat_bp.route("/chat/<roomId>/<userName>")
def chat(roomId, userName):
    if "user" not in session:
        return redirect(url_for("auth.login"))
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
    usersInRoomWithOwner = [
        {
            "name": u.name,
            "id": u.id,
            "rooms": u.rooms,
            "isOwner": room.owner_id == u.id    
        } for u in usersInRoom
    ]
    print(f"niga: {usersInRoomWithOwner}")
        
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
        return render_template("chat.html", users=usersInRoomWithOwner, isCurrentOwnerUser= room.owner_id == user.id, userName=userName)
    return render_template("chat.html", users=usersInRoomWithOwner, messages=messages_with_owner_flag, isCurrentOwnerUser= room.owner_id == user.id, userName=userName)
