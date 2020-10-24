import math

class Ponto:

    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2

    def distancia(self, ponto):
        subx = self.x - ponto.x
        suby = self.y - ponto.y

        return math.sqrt((subx**2)+(suby**2))



class Retangulo:

    def __init__(self, p1, p2):
        self.pie = p1
        self.psd = p2

    def calcula_perimetro(self):
        a = self.pie.x - self.pie.y
        b = self.psd.y - self.pie.y
        
        return (2*a)+(2*b)
    
    def calcula_area(self):
        a = self.psd.x - self.pie.x
        b = self.psd.y - self.pie.y

        return a*b