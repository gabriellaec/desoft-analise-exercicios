from math import sqrt

def distancia_para(self, outro_ponto):
    return sqrt((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)

class Retangulo:
    def __init__(self, p1, p2):
        self.pie = p1
        self.psd = p2
        
    def calcula_perimetro(self):
        a = self.psd.x - self.pie.x
        b = self.psd.y - self.pie.y
        return 2*(a+b)
    
    def calcula_area(self):
        a = self.psd.x - self.pie.x
        b = self.psd.y - self.pie.y
        return a*b
