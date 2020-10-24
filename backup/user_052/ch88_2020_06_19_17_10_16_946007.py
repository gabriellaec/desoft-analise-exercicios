class Retangulo:
    def __init__ (self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
    def calcula_perimetro(self):
        Lado1 = self.ponto1.y - self.ponto2.y
        Lado2 = self.ponto1.x - self.ponto2.x
        Perimetro = 2*Lado1 + 2*Lado2
        return Perimetro
    
    def calcula_area(self):
        Lado1 = self.ponto1.y - self.ponto2.y
        Lado2 = self.ponto1.x - self.ponto2.x
        Area = Lado1 * Lado2
        return Area