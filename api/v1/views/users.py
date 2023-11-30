#!/usr/bin/python3
"""users.py"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User
import hashlib


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """get user information for all users"""
    users = []
    for user in storage.all("User").values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """get user information for specified user"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<string:user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """deletes a user based on its user_id"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """create a new user"""
    # check if user already exists
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'email' not in request.get_json():
        return make_response(jsonify({'error': 'Missing email'}), 400)
    else:
        for user in storage.all("User").values():
            if user.email == request.get_json()['email']:
                return make_response(jsonify({'error': 'Email exists already'}), 400)
    if 'password' not in request.get_json():
        return make_response(jsonify({'error': 'Missing password'}), 400)
    if 'username' not in request.get_json():
        return make_response(jsonify({'error': 'Missing username'}), 400)
    user = User(**request.get_json())
    user.save()
    return make_response(jsonify(user.to_dict()), 201)

@app_views.route('/user/login', methods=['POST'], strict_slashes=False)
def grant_user():
    """Search the user"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'username' not in request.get_json():
        return make_response(jsonify({'error': 'Missing username'}), 400)
    if 'password' not in request.get_json():
        return make_response(jsonify({'error': 'Missing password'}), 400)
    for user in storage.all("User").values():
        if user.username == request.get_json()['username']:
            if hashlib.md5(request.get_json()['password'].encode()).hexdigest() == user.password:
                return make_response(jsonify(user.to_dict()), 201)
            else:
                return make_response(jsonify({'error': 'Incorrect password'}), 400)
    return make_response(jsonify({'error': 'username doesn\'t exist already'}), 400)
    

@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_user(user_id):
    """update a user"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(user, attr, val)
    user.save()
    return jsonify(user.to_dict())