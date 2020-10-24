class Retangulo:
    ponto1 = Ponto()
    ponto2 = Ponto()
    def __init__(self, ponto1, ponto2):
        self.ponto1.x = x
        self.ponto1.y = y
        self.ponto2.x = x
        self.ponto2.y = y
    def calcula_perimetro(self):
        self.perimetro = (self.ponto2.x-self.ponto1.x)*2 + (self.ponto2.y-self.ponto1.y)*2
        return self.perimetro
    
    def calcula_area(self):
        self.area = (self.ponto2.x-self.ponto1.x)*(self.ponto2.y-self.ponto2.y)
        return self.area