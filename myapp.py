from flask import Flask
from manager import ClientContext

class ExtendedApp(Flask):
    clientContext: ClientContext
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        