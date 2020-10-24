class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        
    def calcula_perimetro(self):
        a1 = ponto1.x - self.ponto1.x
        a2 = ponto2.y - self.ponto2.y
        perimetro = a1*2 + a2*2
        return perimetro
        
    def calcula_area(self):
        a1 = ponto1.x - self.ponto1.x
        a2 = ponto2.y - self.ponto2.y
        area = a1*a2
        return area
        