class Retangulo:
    def __init__(self, a, b):
        self.pontoSUP = a
        self.pontoINF = b
    def calcula_perimetro(self):
        self.Z = Ponto
        self.W = Ponto
        dy = self.Z.y - self.W.y
        dx = self.Z.x - self.W.x
        return 2*dx + 2*dy
    def calcula_area(self):
        dy = self.Z.y - self.W.y
        dx = self.W.x - self.W.x
        return dx*dy
    
    