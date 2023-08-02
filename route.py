from flask import Blueprint, jsonify
from app_factory import app
from manager import Movie

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/set")
def movies():
    movie_1 = Movie()
    movie_2 = Movie()
    app.clientContext.setMovies([movie_1, movie_2])
    return jsonify({
        "ok": "movies set"
    })

@api_bp.route('/get')
def test():
    movies = app.clientContext.getMovies()
    
    return jsonify({
        "movies": movies
    })
