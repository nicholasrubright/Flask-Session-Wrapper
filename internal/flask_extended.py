from flask import Flask
import context


class FlaskExtended(Flask):
    clientCtx: context.ClientContext
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)