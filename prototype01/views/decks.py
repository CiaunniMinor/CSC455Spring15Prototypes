# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import request, jsonify, abort, Blueprint
import models

mod = Blueprint('deck', __name__)

# retrieve multiple
@mod.route('/decks', methods=['GET'])
def get_decks():
    return jsonify({'decks': []})

# retrieve individual
@mod.route('/decks/<id>', methods=['GET'])
def get_deck():
    return jsonify({'deck': None})

# create
@mod.route('/decks', methods=['POST'])
def create_deck():
    return jsonify({'deck': []})

# update
@mod.route('/decks/<id>', methods=['POST'])
def update_deck():
    return jsonify({'deck': []})

# delete
@mod.route('/decks/<id>', methods=['POST'])
def delete_deck():
    return jsonify({'deck': []})