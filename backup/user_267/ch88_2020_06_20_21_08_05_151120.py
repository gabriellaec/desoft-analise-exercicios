class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.dx = self.ponto1.x - self.ponto2.x
        self.dy = self.ponto1.y - self.ponto2.y
    def calcula_perimetro(self):
        return ((self.dx*2) + (self.dy*2))
    def calcula_area(self):
        return (self.dx*self.dy)
       
        
       