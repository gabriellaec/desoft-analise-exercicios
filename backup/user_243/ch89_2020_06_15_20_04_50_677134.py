class Circulo:
    def __init__(self,ponto,raio):
        self.ponto = ponto
        self.raio = raio
    def contem(self,ponto):
        p1 = (ponto.x-self.ponto.x)**2
        p2 = (ponto.y-self.ponto.y)**2
        d = (p1+p2)++(0.5)
        return distancia
    