class Circulo:
    def __init__(self, centro, raio):
        self.c = centro
        self.r = raio
    def contem(self, ponto):
        self.p = ponto
        tmp1 = (self.p.x - self.c.x)**2
        tmp2 = (self.p.y - self.c.y)**2
        distancia = (tmp1 + tmp2) ** (1/2)
        if distancia > self.r:
            return False
        return True