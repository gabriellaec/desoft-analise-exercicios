class Circulo():
    
    def __init__(self, centro, raio):
        self.raio = raio
        self.centro = centro
    
    def contem(self, ponto):
        if ((self.centro.x + self.ponto.x)**2 + (self.centro.y + self.ponto.y)**2)**0.5 <= self.raio:
            return True
        else:
            return False
        
        