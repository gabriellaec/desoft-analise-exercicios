class Circulo:
    
    def __init__(self, c, r):
        self.centro = c
        self.raio = r
        
    def contem(self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False