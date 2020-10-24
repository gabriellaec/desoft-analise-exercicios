class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio     
    def contem(self, ponto):
        x = self.centro
        y = self.centro
        a = self.ponto
        b = self.ponto
        if (x - a)**2 +(y - b)**2 <= raio**2:
            return True