class Retangulo:
    def __init__(self,esq,dir):
        self.esquerdo = esq
        self.direito = dir
    def calcula_perimetro(self):
        lado = self.direito.x - self.esquerdo.x
        altura = self.direito.y - self.esquerdo.y
        return 2*(lado+altura)
    def calcula_area(self):
        lado = self.direito.x - self.esquerdo.x
        altura = self.direito.y - self.esquerdo.y
        return lado*altura