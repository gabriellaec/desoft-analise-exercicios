class Circulo():
    
    def __init__(self, raio, centro):
        self.raio = raio
        self.centro = centro
    
    def contem(self, ponto):
        if ((ponto.x - self.centro.x)**2 + (ponto.y - self.centro.y)**2)**0.5 < self.raio:
            return True
        else:
            return False
        
        