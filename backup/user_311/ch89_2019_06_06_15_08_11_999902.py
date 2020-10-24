class Circulo:
    def __init__(self, ponto, raio):
        self.x = ponto.x
        self.y = ponto.y
        self.Raio = raio
    def contem(self, ponto):
        if (self.x - ponto.x)**2 + (self.y - ponto.y)**2 <= self.Raio**2:
            return True
        else:
            return False
        