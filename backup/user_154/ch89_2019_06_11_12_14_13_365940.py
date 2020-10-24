class Circulo:
    
    def __init__(self, centro, raio):
        self.centro = centro
        self.centro_x = centro.x
        self.centro_y = centro.y
        self.raio = raio
    
    def contem(self, ponto):
        return self.raio**2 <= abs(ponto.x - self.centro_x)**2 + abs(ponto.y - self.centro_y)**2