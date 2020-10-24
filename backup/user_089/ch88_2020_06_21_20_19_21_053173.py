class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.a1 = ponto1.x
        self.b1 = ponto1.y
        self.a2 = ponto2.x
        self.b2 = ponto2.y
        def calcula_perimetro(self):
        self.perimetro = (self.a2-self.a1)*2 + (self.b2-self.b1)*2
            return self.perimetro
    
    def calcula_area(self):
        self.area = (self.a2-self.a1)*(self.b2-self.b1)
            return self.area