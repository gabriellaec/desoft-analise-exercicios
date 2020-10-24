import math

class Circulo:
    
    def __init__(self,ponto,raio):
        
        self.center = ponto
        
        self.radius = float(raio)
        
    def contem(self, ponto):
        
        if math.sqrt((self.center.x - ponto.x)**2 + (self.center.y - ponto.y)**2) <= self.radius:
            return True
        else:
            return False