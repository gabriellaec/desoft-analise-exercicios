class Circulo:
    def __init__(self,c,r):
        self.c=centro
        self.r=raio
    def contem(self, ponto):
        if self.centro.distance_to(ponto)<self.raio:
            return True 
        else:
            return False