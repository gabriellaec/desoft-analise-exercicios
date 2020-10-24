
class Distancia:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia_pontos(self, outro_ponto):
        b = ((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)
        return b
      

class Circulo:
    def __init__(self, centro, raio):
        self.centro =  centro
        self.raio = raio
    def contem(self, ponto):
        if self.centro.distancia_pontos(ponto) <= self.raio:
            return True
        else:
            return False