import math

class Circulo:
    
    def __init__(self, p1, p2):
        self.centro = p1
        self.raio = p2
    
    def contem(self, ponto):
        c1 = (self.centro.x - ponto.x)**2
        c2 = (self.centro.y - ponto.y)**2
        
        h = c1 + c2
        
        if h > self.raio:
            return False
        else:
            return True
        