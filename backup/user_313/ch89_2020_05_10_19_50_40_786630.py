class Circulo:
    
    def __init__(self, centro1, raio1):
        self.centro = centro1
        self.raio = float(raio1)
        
    def distance_to(self, ponto):
        subx = (self.x - ponto.x)**2
        suby = (self.y - ponto.y)**2

        return math.sqrt(subx+suby)
        
    def contem(self, ponto):
        if self.centro < self.raio:
            return True
        else:
            return False