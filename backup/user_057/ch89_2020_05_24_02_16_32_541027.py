class Circulo:
    def __init__(self, ponto, raio):
        self.centro = ponto
        self.raio = raio
    
    def contem(self, ponto):
        dx = ponto.x - self.x
        dy = ponto.y - self.y
        d = ((dx**2) + (dy**2)) ** 0.5
        if d < self.raio:
            return True
        else:
            return False
        