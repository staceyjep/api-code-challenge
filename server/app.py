from flask import Flask, jsonify
from flask_migrate import Migrate
from server import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    db.init_app(app)
    Migrate(app, db)
    
    # Add a basic test route
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to Late Show API"})
    
    # Import and register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.appearance_controller import appearance_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(guest_bp, url_prefix='/api')
    app.register_blueprint(episode_bp, url_prefix='/api')
    app.register_blueprint(appearance_bp, url_prefix='/api')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()