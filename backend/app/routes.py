import os
from . import create_app
from .models import *
from flask import jsonify

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route("/surah/list", methods=["GET"])
def get_books():
    books = Surah.query.all()
    return jsonify([book.to_json() for book in books])

@app.route("/surah/<int:isbn>", methods=["GET"])
def get_book(isbn):
    book = Surah.query.get(isbn)
    if book is None:
        abort(404)
    return jsonify(book.to_json())
from . import db
# ...
import datetime
@app.route("/surah/<int:isbn>", methods=["DELETE"])
def delete_book(isbn):
    book = Surah.query.get(isbn)
    if book is None:
        abort(404)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'result': True})
from flask import request
...

@app.route('/logs', methods=['POST'])
def create_book():
    if not request.json:
        abort(400)
    log = Logs( 
        title=request.json.get('title'),
        datetime.now(),
        author=request.json.get('author'),
        price=request.json.get('price')
    )
    db.session.add(log)
    db.session.commit()
    return jsonify(book.to_json()), 201