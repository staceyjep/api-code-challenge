from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    """Create new appearance (protected route)"""
    data = request.get_json()
    
    # Validate required fields
    if not all(key in data for key in ['rating', 'guest_id', 'episode_id']):
        return jsonify({"error": "Missing required fields"}), 400
    
    appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201