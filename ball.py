import pygame
from settings import pixelsPerMetre as px
from settings import GRAVITY, airResistance

class projectile():
    def __init__(self, x, y, rad):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.rad = rad
        self.onFloor = False
        self.thrown = False
        self.placed = False

    def applyGravity(self, dt):
        if  not self.onFloor and self.thrown:
            self.vel.y += GRAVITY * dt
        elif self.onFloor:
            self.vel.y = -(self.vel.y * 0.5)

    def applyMovement(self, floor, dt):
        keys = pygame.key.get_pressed()

        self.vel.x = max(-(100*px), min(self.vel.x, (100 * px)))

        if self.thrown:
            self.pos += self.vel * dt
            self.vel.x *= airResistance
        if self.pos.y > floor - self.rad:
            self.pos.y = floor - self.rad
            self.onFloor = True
        else:
            self.onFloor = False
        # print(int(self.vel.y / px))
        if self.pos.x < self.rad:
            self.pos.x = self.rad
            self.vel.x = -(self.vel.x * 0.75)
        if self.pos.x > 1280 - self.rad:
            self.pos.x = 1280 - self.rad
            self.vel.x = -(self.vel.x * 0.75)

    def draw(self, screen):
        if self.placed:
            pygame.draw.circle(screen, (128, 255, 10), self.pos, self.rad)

    def update(self, dt, screen, floor):
        self.applyGravity(dt=dt)
        self.applyMovement(floor=floor, dt=dt)
        self.draw(screen=screen)


