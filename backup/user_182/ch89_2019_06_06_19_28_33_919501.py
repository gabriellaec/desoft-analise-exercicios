class Circulo:
    def __init__(self, raio, ponto):
        self.x = ponto.x
        self.y = ponto.y
        self.raio = raio
    def contem(self, ponto):
        if (self.x - ponto.x)**2 + (self.y - ponto.y)**2 == self.raio **2:
            return True
        else:
            return False