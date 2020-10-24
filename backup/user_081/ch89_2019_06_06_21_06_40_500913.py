class Circulo:
    def __init__(self, centro,raio):
        self.centrox = centro.x
        self.centroy = centro.y
        self.raio = raio
    def contem(self,ponto):
        if (self.centrox-ponto.x)**2+(self.centroy-ponto.y)**2<=self.raio**2:
            return True
        else:
            return False
        