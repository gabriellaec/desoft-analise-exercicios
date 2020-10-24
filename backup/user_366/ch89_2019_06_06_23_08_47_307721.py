class Circulo():
    
    def __init__(self, raio, centro):
        self.raio = raio
        self.x = centro.x
        self.y = centro.y
    
    def contem(self, ponto):
        if (ponto.x - self.x)**2 + (ponto.y - self.y)**2 < self.raio**2:
            return True
        else:
            return False
        
        