class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1o = ponto1
        self.ponto2o = ponto2
        self.dx = self.ponto1o.x - self.ponto2o.x
        self.dy = self.ponto1o.y - self.ponto2o.y
    def calcula_perimetro(self):
        return ((self.dx*2) + (self.dy*2))
    def calcula_area(self):
        return self.dx*self.dy
       
        
       