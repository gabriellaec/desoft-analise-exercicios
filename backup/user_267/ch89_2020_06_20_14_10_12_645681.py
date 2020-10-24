import math
class Circulo:
    def __init__(self, ponto,raio):
        self.ponto = ponto
        self.raio = raio
    def contem(self, ponto):
        distx = self.ponto.x - ponto.x
        disty = self.ponto.y - ponto.y
        d = ((distx**2)+(disty**2))**0.5
        if d <= (self.raio): 
            return True
        else:
            return False
        






























        
        
    