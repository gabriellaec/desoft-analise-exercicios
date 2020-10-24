class Retangulo:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2
    def calcula_perimetro(self):
        if (self.P1.x == P2.x) or (self.P1.y == P2.y):
            return 0
        return 2*abs(self.P1.x - self.P2.x) + 2*abs(self.P1.y - self.P2.y)
    
    def calcula_area(self):
        return abs(self.P1.x - self.P2.x)*abs(self.P1.y -self.P2.y)