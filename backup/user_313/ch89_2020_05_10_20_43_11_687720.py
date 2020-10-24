import math

class Circulo:
    
    def __init__(self, p1, p2):
        self.centro = p1
        self.raio = p2
    
    def distancia(self):
        subx = self.ponto.x - self.raio
        suby = self.ponto.y - self.raio
        
        return [subx, suby]
        

    def contem(self,ponto):
        self.ponto = ponto
        
        x = self.distancia()
        primeiro  = x[0]
        segundo   = x[1]
        
        if primeiro > self.raio or segundo > self.raio:
            return False
        
        else:
            return True