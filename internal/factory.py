from internal.flask_extended import FlaskExtended
from context import ClientContext
from routes import api_bp

def create_app(name: str = __name__) -> FlaskExtended:
    
    app = FlaskExtended(name)
    
    app.secret_key = b'secret'
    app.clientCtx = ClientContext()
    
    app.register_blueprint(api_bp)
    
    return app