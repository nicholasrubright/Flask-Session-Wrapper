from flask import session
from typing import List
class Movie:
    id = 1
    title = "Test Movie"
    
    def __dict__(self):
        return {"id": self.id, "title": self.title}

class SessionKeys:
    MOVIES = "MOVIES"
    CURRENT_INDEX = "CURRENT_INDEX"

class ClientContext:
        
    def getMovies(self):
        movies = []
        if SessionKeys.MOVIES in session:
            movies = list(session[SessionKeys.MOVIES])
        
        return movies

    
    def setMovies(self, movies: List[Movie]):
        sessionMovies = []
        for movie in movies:
            sessionMovies.append(movie.__dict__())
        session[SessionKeys.MOVIES] = sessionMovies
        
             
    