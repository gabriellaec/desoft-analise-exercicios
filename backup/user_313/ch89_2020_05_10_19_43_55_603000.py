class Circulo:
    
    def __init__(self, centro1, raio1):
        self.centro = centro1
        self.raio = float(raio1)
        
    def contem(self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False