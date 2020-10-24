class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        
    def calcula_perimetro(self):
        p = 2 * ((self.ponto2.x - self.ponto1.x) + (self.ponto2.y - self.ponto1.y))
        return p
 
    def calcula_area(self):
        a = (self.ponto2.x - self.ponto1.x) * (self.ponto2.y - self.ponto1.y)
        return a