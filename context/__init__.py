from flask import session
from typing import List
from models import Movie

class SessionKeys:
    MOVIES = "MOVIES"

class ClientContext:
    
    def getMovies(self) -> List[Movie]:
        movies = []
        if SessionKeys.MOVIES in session:
            movies = list(session[SessionKeys.MOVIES])
        
        return movies

    
    def setMovies(self, movies: List[Movie]):
        sessionMovies = []
        for movie in movies:
            sessionMovies.append(movie.__dict__)
        session[SessionKeys.MOVIES] = sessionMovies