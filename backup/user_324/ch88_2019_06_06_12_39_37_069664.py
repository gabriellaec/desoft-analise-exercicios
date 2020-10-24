class Retangulo:
    def _init_(self, Ponto1, Ponto2):
        self.Ponto1=Ponto1
        self.Ponto2=Ponto2
    def calcula_perimetro(self):
        return (2*self.Ponto1 + 2*self.Ponto2)
    def calcula_area(self):
        return (self.Ponto1*self.Ponto2)
    