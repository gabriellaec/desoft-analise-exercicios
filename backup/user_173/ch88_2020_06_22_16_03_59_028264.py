class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        
    def calcula_perimetro(self):
        perimetro = abs(self.ponto1.y - self.ponto2.y)*2 + abs(self.ponto1.x - self.ponto2.x)*2
        return perimetro
    
    def calcula_area(self):
        area = abs(self.ponto1.y - self.ponto2.y) * abs(self.ponto1.x - self.ponto2.x)
        return area
        