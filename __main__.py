import pygame
import random
import numpy as np

from src.quadtree import *
from src.particle import Particle

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)

    FramePerSec = pygame.time.Clock()
    running = True

    particles = []

    for i in range(0, 1000):
        particles.append(Particle(random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)))

    while running:

        boundary = Rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        qtree = QuadTree(boundary, 4)

        screen.fill(BLACK)

        for p in particles:
            p.move()
            point = Point(p.x, p.y, p)
            qtree.insert(point)
            if p.highlight:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.circle(screen, color, (p.x, p.y), p.r, 1)
            p.setHighlight(False)
        # qtree.show(screen, BLUE)

        for p in particles:
            new_range = Circle(p.x, p.y, p.r * 2)
            points = qtree.query(new_range)
            for point in points:
                other = point.userData
                if p != other and p.intersects(other):
                    p.setHighlight(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main()
