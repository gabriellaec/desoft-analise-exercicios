class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.canto1x= ponto1.x
        self.canto1y= ponto1.y
        self.canto2x= ponto2.x
        self.canto2y= ponto2.y
        self.width= abs(ponto1.x - ponto2.x)
        self.lenght= abs(ponto1.y - ponto2.y)
        
    def calcula_perimetro(self):
        return 2*(self.width + self.lenght)
    def calcula_area(self):
        return self.lenght*self.width