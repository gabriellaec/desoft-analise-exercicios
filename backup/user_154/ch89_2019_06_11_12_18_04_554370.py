class Circulo:
    
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, ponto):
        return self.raio**2 >= abs(ponto.x - self.centro.x)**2 + abs(ponto.y - self.centro.y)**2