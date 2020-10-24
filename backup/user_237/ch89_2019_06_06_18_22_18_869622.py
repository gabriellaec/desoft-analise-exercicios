class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
        
    def contem(self, ponto):
        d =(ponto.y - self.centro.y)**2 + (ponto.x - self.centro.x)**2 
        if self.raio >= d**2:
            return True
        else:
            return False