from flask import Blueprint, render_template, redirect, session, url_for

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    if "user" in session:
        return redirect(url_for("chat.chatRooms", user=session["user"]))
    return render_template("home.html")