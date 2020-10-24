import math

class Circulo:
    
    def __init__(self, p1, p2, ponto):
        self.centro = p1
        self.raio = p2
        self.ponto = ponto
    
    def contem(self, ponto):
        resultado = self.ponto.x - self.centro.x
        
        if resultado > self.raio:
            return False
        else:
            return True
        
    def contem(self,ponto):
        self.ponto = ponto
        
        x = self.distancia()
        primeiro  = x[0]
        segundo   = x[1]
        
        if primeiro > self.raio or segundo > self.raio:
            return False
        
        else:
            return True