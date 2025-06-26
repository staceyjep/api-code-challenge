from flask import Blueprint, jsonify, request
from server.models.guest import Guest
from server import db
from flask_jwt_extended import jwt_required

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_all_guests():
    """Get all guests (no auth required)"""
    guests = Guest.query.all()
    return jsonify([{
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation,
        'appearances': len(guest.appearances)
    } for guest in guests]), 200

@guest_bp.route('/guests/<int:guest_id>', methods=['GET'])
def get_guest(guest_id):
    """Get specific guest with appearances (no auth required)"""
    guest = Guest.query.get_or_404(guest_id)
    return jsonify({
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation,
        'appearances': [{
            'episode_id': appearance.episode_id,
            'rating': appearance.rating,
            'episode_date': appearance.episode.date.isoformat()
        } for appearance in guest.appearances]
    }), 200

@guest_bp.route('/guests', methods=['POST'])
@jwt_required()
def create_guest():
    """Create new guest (auth required)"""
    data = request.get_json()
    
    # Validate required fields
    if not data.get('name'):
        return jsonify({"error": "Name is required"}), 400
    
    guest = Guest(
        name=data['name'],
        occupation=data.get('occupation', '')
    )
    
    db.session.add(guest)
    db.session.commit()
    
    return jsonify({
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    }), 201