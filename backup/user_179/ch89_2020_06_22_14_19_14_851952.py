class Circulo:
    def __init__(self,centro,raio):
        self.centro = centro
        self.raio = raio
    def contem(self,ponto):
        dx = ponto.x - self.centro.x
        dy = ponto.y - self.centro.y
        distancia = ((dx**2) + (dy**2)) ** 0.5
        if distancia > self.raio:
            return False
        else:
            return True