from flask import Blueprint, jsonify
from models import Movie

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/set")
def movies():
    movie_1 = Movie(1, "Awesome Movie")
    movie_2 = Movie(2, "Another awesome movie")
    from internal.app import app
    app.clientCtx.setMovies([movie_1, movie_2])
    return jsonify({
        "ok": "movies set"
    })

@api_bp.route('/get')
def test():
    from internal.app import app
    movies = app.clientCtx.getMovies()
    return jsonify({
        "movies": movies
    })
