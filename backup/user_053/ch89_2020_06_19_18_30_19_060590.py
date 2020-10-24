from math import sqrt
class Circulo:
    def __init__(self):
        self.centro = (0, 0)
        self.raio = 5
    
    def contem(self, ponto):
        if (abs((ponto.x - self.centro.x) + (ponto.y - self.centro.y)) > self.raio):
            return True
        else: 
            return False