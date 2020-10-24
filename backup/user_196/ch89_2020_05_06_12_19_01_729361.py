class Circulo:
    def __init__(self, ponto, raio):
        self.ponto = ponto
        self.raio = raio    
    def contem(self, ponto):
        x = self.ponto
        y = self.ponto
        a = self.ponto
        b = self.ponto
        if (x - a)**2 +(y - b)**2 <= raio**2:
            return True