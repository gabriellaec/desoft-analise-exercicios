

class Circulo:
    def __init__(self, centro, raio):
        self.c=centro
        self.r=raio
    def contem(self, ponto):
        if self.c.distancia(ponto) < self.r:
            return True
        else:
            return False
        