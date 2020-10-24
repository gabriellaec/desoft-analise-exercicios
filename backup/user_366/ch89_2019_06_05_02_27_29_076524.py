class Circulo():
    
    def __init__(self, raio, centro):
        self.raio = raio
        self.centro = centro
    
    def contem(self, ponto):
        if ((self.centro.x + ponto.x)**2 + (self.centro.y + ponto.y)**2)**0.5 < self.raio:
            return True
        else:
            return False
        
        