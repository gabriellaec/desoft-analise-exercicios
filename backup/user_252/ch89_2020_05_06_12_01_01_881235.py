def distancia(self, outro):
    dx=outro.x-self.x
    dy=outro.y-self.y
    return ((dx**2)+(dy**2))**0.5

class Circulo:
    def __init__(self, centro, raio):
        self.c=centro
        self.r=raio
    def contem(self, ponto):
        if self.c.distancia(ponto) < self.r:
            return True
        else:
            return False
        