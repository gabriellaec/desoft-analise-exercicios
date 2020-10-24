class Circulo:
    def __init__(self, ponto, raio):
        self.ponto = ponto
        self.raio = raio
    def contem(self,ponto):
        d1 = (ponto.x - self.ponto.x)**2
        d2 = (ponto.y - self.ponto.y)**2
        distancia = (d1+d2)**(1/2)
        if distancia > self.raio:
            return False
        return True