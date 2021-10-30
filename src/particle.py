import math
import random
import pygame

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 4
        self.highlight = False

    def intersects(self, other):
        d = math.dist((self.x, self.y), (other.x, other.y))
        return d < self.r + other.r

    def setHighlight(self, value):
        self.highlight = value

    def move(self):
        if self.x == 600:
            self.x = 0
        elif self.x == 0:
            self.x = 600
        elif self.y == 600:
            self.y = 0
        elif self.y == 0:
            self.y = 600
            
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)