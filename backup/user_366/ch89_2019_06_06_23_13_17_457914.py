class Circulo():
    
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, ponto):
        if (ponto.x - self.centro.x)**2 + (ponto.y - self.centro.y)**2 < self.raio**2:
            return True
        else:
            return False
        
        