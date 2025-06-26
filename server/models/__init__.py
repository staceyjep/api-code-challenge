# Import db FIRST
from server import db

# Then import models
from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance

__all__ = ['User', 'Guest', 'Episode', 'Appearance']