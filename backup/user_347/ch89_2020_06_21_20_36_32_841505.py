class Circulo:
    def __init__(self, centro, raio):
        self.c = centro
        self.r = raio
    def contem(self, ponto):
        tmp1 = (ponto.x - self.c.x)**2
        tmp2 = (ponto.y - self.c.y)**2
        distancia = (tmp1 + tmp2) ** (1/2)
        if distancia > self.raio:
            return False
        return True