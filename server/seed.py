from server import create_app
from server.models import db, User, Guest, Episode, Appearance
from datetime import date

app = create_app()

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create test user
    user = User(username='admin')
    user.set_password('password')
    db.session.add(user)

    # Create sample data
    guests = [
        Guest(name='John Mulaney', occupation='Comedian'),
        Guest(name='Emma Stone', occupation='Actor')
    ]
    db.session.add_all(guests)

    episodes = [
        Episode(date=date(2023, 1, 1), number=101),
        Episode(date=date(2023, 1, 2), number=102)
    ]
    db.session.add_all(episodes)

    appearances = [
        Appearance(rating=5, guest_id=1, episode_id=1),
        Appearance(rating=4, guest_id=2, episode_id=2)
    ]
    db.session.add_all(appearances)

    db.session.commit()
    print("Database seeded successfully!")