class Circulo:
    def __init__(self, ponto, raio):
        self.ponto = ponto
        self.raio = raio
        
    def contem(self, ponto):
        tmp1 = (ponto.x - self.ponto.x)**2
        tmp2 = (ponto.y - self.ponto.y)**2
        distancia = (tmp1 + tmp2) ** (1/2)
        if distancia > self.raio:
            return False
        else:
            return True