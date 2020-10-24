class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def contem (self, ponto):
        deltax = self.centro.x - ponto.x 
        deltay = self.centro.y - ponto.y
        distancia = ((deltax**2)+(deltay2))*0.5
        return distancia <= self.raio