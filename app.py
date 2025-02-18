from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Movie

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message":"Que tal Mundo!"})

@app.route("/movies", methods=["GET"])
def get_movies():
    movies = Movie.query.all()
    #return jsonify([movie.to_dict() for movie in movies])
    ret = []
    for x in movies:
        ret.append(x.to_dict())
    return jsonify(ret), 200

@app.route("/movies", methods=["POST"])
def create_movie():
    data = request.get_json()
    title = data.get("title")
    year = 0
    try:
        year = int(data.get("year"))
    except ValueError:
        return jsonify({"error": "Invalid year"}), 400

    if not title or not year:
        return jsonify({"error": "Missing data"}), 400

    movie = Movie(title=title, year=year)
    db.session.add(movie)
    db.session.commit()

    return jsonify(movie.to_dict()), 201


@app.route("/movies/<int:id>", methods=["GET"])
def get_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    return jsonify(movie.to_dict()), 200

@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    data = request.get_json()
    movie.title = data.get("title")
    movie.year = data.get("year")
    db.session.commit() 
    return jsonify(movie.to_dict()), 200


@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    db.session.delete(movie)
    db.session.commit() 
    return jsonify(movie.to_dict()), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="0.0.0.0")


""" tarea

hace el put (update) y el delete





"""