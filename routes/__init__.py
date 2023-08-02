from flask import Blueprint, jsonify
import models
import internal.app

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/set")
def movies():
    movie_1 = models.Movie(1, "Awesome Movie")
    movie_2 = models.Movie(2, "Another awesome movie")
    internal.app.app.clientCtx.setMovies([movie_1, movie_2])
    return jsonify({
        "ok": "movies set"
    })

@api_bp.route('/get')
def test():
    movies = internal.app.app.clientCtx.getMovies()
    return jsonify({
        "movies": movies
    })
