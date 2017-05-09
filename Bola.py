import globals
import pygame


class Ball():

    def __init__(self, x, y, vx=0, vy=0, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.width = 5
        self.height = 5
        self.color = color

    # Bounce off of walls with inelastic collisions
    def collide_walls(self):
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
        if self.x > globals.width - self.width:
            self.x = globals.width - self.width
            self.vx = -self.vx
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
        if self.y > globals.height - self.height:
            self.y = globals.height - self.height
            self.vy = -self.vy * 0.8

    def update(self):
        # Apply friction
        self.vx -= self.vx * globals.friction
        # Apply gravity
        self.vy += globals.gravity
        # Move ball
        self.x += self.vx
        self.y += self.vy
        self.collide_walls()

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(globals.window, self.color, rect)
