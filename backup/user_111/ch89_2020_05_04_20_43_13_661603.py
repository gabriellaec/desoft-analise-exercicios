import math
class Circulo:
    def __init__(self,centro,raio):
        self.centro=centro
        self.raio=raio
        
    def contem(self,ponto):
        distancia=((self.ponto.x-self.centro.x)**2-(self.ponto.y-self.centro.y)**2)**0.5
        if distancia>raio:
            return False
        else:
            return True