from math import sqrt

class Point:
    def __init__(self, vx, vy): 
        self.x = vx 
        self.y = vy
    def distance_to(self, other_point):
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

class Retangulo:
    def __init__(self, p1, p2): 
        self.pie = p1 
        self.psd = p2
    def perimetro(self): 
        a = self.psd.x - self.pie.x 
        b = self.psd.y - self.pie.y 
        return 2 * (a + b)
    def area(self): 
        a = self.psd.x - self.pie.x 
        b = self.psd.y - self.pie.y 
        return a * b