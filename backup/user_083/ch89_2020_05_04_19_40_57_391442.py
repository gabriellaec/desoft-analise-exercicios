from math import sqrt
class Circulo:
    def __init__(self,centro,raio):
        self.centro=centro
        self.raio=raio
    def distance_to(self,op):
        return sqrt((self.x-op.x)**2 + (self.y-op.y)**2)
    def contem(self,ponto):
        if self.centro.distance_to(ponto)<self.raio:
            return True 
        else:
            return False