class Circulo:
    def _init_(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def contem (self, ponto):
        deltax = self.centro.x - ponto.x 
        deltay = self.centro.y - ponto.y
        distancia = ((deltax**2)+(deltay*2))*0.5
        return distancia <= self.raio