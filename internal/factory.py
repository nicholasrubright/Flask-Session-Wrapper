from internal import FlaskExtended
from context import ClientContext
from routes import api_bp

def create_app() -> FlaskExtended:
    
    app = FlaskExtended(__name__)
    
    app.secret_key = b'secret'
    app.clientCtx = ClientContext()
    
    app.register_blueprint(api_bp)
    
    return app