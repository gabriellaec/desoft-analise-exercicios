class Circulo:
    def __init__(self, centro, raio):
        
        self.centro = centro
        self.raio = raio
        
    def contem(self, ponto):
        
        self.ponto = ponto
        
        dx = (self.centro.x - self.ponto.x) ** 2
        dy = (self.centro.y - self.ponto.y) ** 2
        d = (dx + dy) ** (1/2)
        if d < self.raio:
            return True
        else:
            return False
    