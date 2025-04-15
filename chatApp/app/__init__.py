from flask_sqlalchemy import SQLAlchemy
import socketio
from flask import Flask
from datetime import timedelta

#Tady se vytvoří Flask appka, nastaví se databáze, session a propojí Socket.IO. Taky to načítá routy a sockety z oddělených souborů.

db = SQLAlchemy() #db = SQLAlchemy(app), to app tam neni protože db musí bejt dostupná i bez appky, to je potřeba kvůli modularizaci
sio = socketio.Server()

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.secret_key = "hello"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatApp.db"
    app.config["SQLALCHEMY_TRACK_MODOFICATIONS"] = False
    app.permanent_session_lifetime = timedelta(days=1)
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    
    db.init_app(app)    #připojení db k appce, db je potřeba globálně kvůli modularizaci
    
    # Registrace routek a socketů
    from .routes import register_blueprints
    register_blueprints(app)
    
    from .sockets import register_socket_events
    register_socket_events(sio, app)
    
    with app.app_context():
        db.create_all()
    
    return app
    
    
def sio_app(app):
        return socketio.WSGIApp(sio, app)   #tempaltes už opbsarává Flask app, takže stačí napsat tohle, to ze starýho je spíš na js frontend a websocket projekt což není můj případ
    
    