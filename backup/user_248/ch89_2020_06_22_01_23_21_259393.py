import math          
class Circulo:
    def __init__(self,ponto,raio):
        self.ponto= ponto
        self.raio= raio
    
    def contem(self, ponto):
        if ((ponto.x - self.ponto.x)**2 + (ponto.y - self.ponto.y)**2)**0.5 < self.raio:
            return True
        else:
            return False
                   