from circleshape import *
from constants import *

shots = pygame.sprite.Group()

class Shot(CircleShape):
    containers = (shots,)
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.math.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt