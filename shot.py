from circleshape import *
from constants import *

class Shot(CircleShape):
    containers = None
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        velocity = 0