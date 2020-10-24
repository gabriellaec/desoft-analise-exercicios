import math

class Circulo:
    
    def __init__(self, p1, p2):
        self.centro = p1
        self.raio = p2
    
    def distancia(self):
        subx = self.centro.x - self.raio
        suby = self.centro.y - self.raio
        
        return [subx, suby]
        

    def contem(self,distancia):
        x = self.distancia()
        primeiro  = x[0]
        segundo   = x[1]
        
        if primeiro > self.raio or segundo > self.raio:
            return False
        
        else:
            return True