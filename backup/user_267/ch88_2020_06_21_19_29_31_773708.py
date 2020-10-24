class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.dx = ponto2.x - ponto1.x
        self.dy = ponto2.y - ponto1.y
    def calcula_perimetro(self):
        perimetro = ((self.dx*2)+(self.dy*2))
        return perimetro
    def calcula_area(self):  
        area = ((self.dx)*(self.dy))
        return area
       