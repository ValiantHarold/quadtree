import math
import pygame

class Point:

    def __init__(self, x, y, userData):
        self.x, self.y = x, y
        self.userData = userData
    
class Rectangle:

    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

    def contains(self, point):
        return (
            point.x >= self.x - self.w and
            point.x <= self.x + self.w and
            point.y >= self.y - self.h and
            point.y <= self.y + self.h
        )

    def intersects(self, range):
        return not(
            range.x - range.w > self.x + self.w or
            range.x + range.w < self.x - self.w or
            range.y - range.h > self.y + self.h or
            range.y + range.h < self.y - self.h
        )

class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.rSquared = self.r * self.r

    def contains(self, point):
        d = math.pow(point.x - self.x, 2) + math.pow(point.y - self.y, 2)
        return d <= self.rSquared

    def intersects(self, range):
        xDist = abs(range.x - self.x)
        yDist = abs(range.y - self.y)

        r = self.r

        w = range.w
        h = range.h

        edges = math.pow(xDist - w, 2) + math.pow(yDist - h, 2)

        if xDist > r + w or yDist > r + h:
            return False

        if xDist <= w or yDist <= h:
            return True

        return edges <= self.rSquared

class QuadTree:

    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):

        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w / 2
        h = self.boundary.h / 2

        ne = Rectangle(x + w, y, w, h)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x, y, w, h)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + w, y + h, w, h)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x, y + h, w, h)
        self.southwest = QuadTree(sw, self.capacity)

        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False
    

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        
        if not self.divided:
            self.subdivide()
    

        if (
            self.northeast.insert(point) or
            self.northwest.insert(point) or
            self.southeast.insert(point) or
            self.southwest.insert(point)
        ):
            return True
    
    def query(self, range, found = None):
        if found is None:
            found = []
    
        if not range.intersects(self.boundary):
            return found
        
        for p in self.points:
            if range.contains(p):
                found.append(p)
      
        if self.divided:
            self.northeast.query(range, found)
            self.northwest.query(range, found)
            self.southeast.query(range, found)
            self.southwest.query(range, found)
    
        return found

    def show(self, screen, color):
        pygame.draw.rect(screen, color, (self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h), 1)
   
        if self.divided:
            self.northeast.show(screen, (255,0,0))
            self.northwest.show(screen, (0,255,0))
            self.southeast.show(screen, (0,0,255))
            self.southwest.show(screen, (255,0,255))