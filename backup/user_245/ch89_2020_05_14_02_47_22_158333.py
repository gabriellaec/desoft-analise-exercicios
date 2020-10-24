class Circulo:
    def __init__(self,center,radius):
        self.centro = center
        self.raio = radius
        
    def contem(self, ponto):
        if self.centro(ponto) < self.raio:
            return True
        else:
            return False