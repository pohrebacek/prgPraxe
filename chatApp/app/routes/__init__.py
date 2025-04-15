from .auth import auth_bp
from .main import main_bp
from .chat import chat_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(chat_bp)
