class Retangulo:
    def _init_(self, Ponto1, Ponto2):
        self.Ponto1=Ponto
        self.Ponto2=Ponto2
    def calcula_perimetro(self):
        perimetro = 2*self.Ponto1 + 2*self.Ponto2
        return perimetro
    def calcula_area(self):
        area = self.Ponto1*self.Ponto2
        return area