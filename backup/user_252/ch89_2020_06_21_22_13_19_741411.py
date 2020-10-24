from math import*
class Circulo:
    def __init__(self, ponto, raio):
        self.centro=ponto
        self.raio=raio
    def contem (self, ponto):
        dis=sqrt((self.centro.x - ponto.x)**2+(self.centro.y - ponto.y)**2)
        if dis <= self.raio:
            return True
        else:
            return False

 
    
        