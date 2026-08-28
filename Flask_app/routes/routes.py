from flask import Blueprint, jsonify, request

from services.services import (
    get_all_users,
    get_user_by_id,
    add_user,
    update_user,
    delete_user
)


user_bp = Blueprint("user", __name__)


# Home
@user_bp.route("/", methods=["GET"])
def home():
    return "Flask application is connected"


# Get all users
@user_bp.route("/users", methods=["GET"])
def get_users():

    users = get_all_users()

    return jsonify(users)


# Get user by ID
@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    user = get_user_by_id(user_id)

    if user is None:
        return jsonify({
            "message": "User not found"
        }), 404

    return jsonify(user)


# Add user
@user_bp.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    user_id = add_user(
        data["user_name"],
        data["user_city"],
        data["gender"]
    )

    return jsonify({
        "message": "User added",
        "user_id": user_id
    }), 201


# Update user by ID
@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user_route(user_id):

    data = request.get_json()

    updated = update_user(
        user_id,
        data["user_name"],
        data["user_city"],
        data["gender"]
    )

    if not updated:
        return jsonify({
            "message": "User not found"
        }), 404

    return jsonify({
        "message": "User updated",
        "user_id": user_id
    })


# Delete user by ID
@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user_route(user_id):

    deleted = delete_user(user_id)

    if not deleted:
        return jsonify({
            "message": "User not found"
        }), 404

    return jsonify({
        "message": "User deleted",
        "user_id": user_id
    })