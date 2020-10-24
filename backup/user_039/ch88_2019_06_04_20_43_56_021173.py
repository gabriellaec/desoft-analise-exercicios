class Retangulo:
    def __init__(self, e, d):
        self.ponto1 = e.x
        self.ponto2 = d.y
    def calcula_perimetro(self):
        self.P = (self.ponto1 - self.ponto2)*2
    def calcula_area(self):
        self.a = self.e*self.d
        
        
    