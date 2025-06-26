from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from server.models.user import User
from server import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Your registration logic here
    return jsonify({"message": "Registration endpoint"}), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    # Your login logic here
    return jsonify({"message": "Login endpoint"}), 200