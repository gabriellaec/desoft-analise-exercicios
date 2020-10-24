class Circulo:
    
    def __init__(self, centro, raio):
        self.centro_x = centro.x
        self.centro_y = centro.y
        self.raio = raio
    
    def contem(self, ponto):
        return self.raio**2 <= abs(self.centro_x - ponto.x)**2 + abs(self.centro_y + ponto.y)**2 