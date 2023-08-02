from flask import Flask
from context import ClientContext


class FlaskExtended(Flask):
    clientCtx: ClientContext
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)