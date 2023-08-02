from myapp import ExtendedApp

def create_app() -> ExtendedApp:
    app = ExtendedApp(__name__)
    return app


app = create_app()