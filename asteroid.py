import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
                screen,
                "white",
                self.position,
                self.radius,
                LINE_WIDTH
                )

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # angle of splitting
        angle = random.uniform(20, 50)

        # velocities when splitting
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        # smaller radius
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        # two new asteroids
        a1 = Asteroid(self.position.x, self.position.y, new_rad)
        a2 = Asteroid(self.position.x, self.position.y, new_rad)

        # set two diffent directions for velocity
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
