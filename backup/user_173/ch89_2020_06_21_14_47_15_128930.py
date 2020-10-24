class Circulo:
    def __init__(self,centro,raio):
        self.ponto = ponto
        self.raio = raio
    def contem(self,ponto):
        tmp1 = (ponto.x - self.ponto.x)**2 
        tmp2 = (ponto.y - self.ponto.y)**2 
        distancia = (tmp1 + tmp2)**0.5
        return distancia