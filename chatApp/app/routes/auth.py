from flask import Blueprint, render_template, redirect, request, session, url_for
from .. models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
        session.permanent = True
        user = request.form["nm"]
        
        
        found_user = User.query.filter_by(name=user).first()   #najde všechny users co maj to name, first je protože chceš jenom jednoho user
        if found_user == None:
            return "Špatné přihlašovací údaje", 401
        elif (not found_user.check_password(request.form["password"])):
            return "Špatné přihlašovací údaje", 401
        else:
            session["user"] = user  #přidání do session je až tady protože jinak se ten user přidal do session i když neexistoval a přiskoku zpět na homepage ho to hodilo do chatrooms i když ten user ani neexistoval
            print(f"found user {found_user.name}")
            session["found_userID"] = found_user.id
                    
        print("Entered username saved in session as user: "+session["user"])
        return redirect(url_for("chat.chatRooms", user=user))
    else:
        return render_template("login.html")
    
    

@auth_bp.route("/register", methods=["POST", "GET"])
def register():
    #bude to přes socketio, tohle bude jnom na render
    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.home"))