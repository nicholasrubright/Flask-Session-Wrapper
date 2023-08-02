from route import api_bp
from manager import ClientContext
from app_factory import app

app.secret_key = b'secret'
app.clientContext = ClientContext()
app.register_blueprint(api_bp)


app.run('0.0.0.0', port=8080)