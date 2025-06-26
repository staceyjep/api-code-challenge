from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': e.id,
        'date': e.date.isoformat(),
        'number': e.number
    } for e in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200