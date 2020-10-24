class Retangulo:
    def __init__(self,p1,p2):
        self.pontoa = p1
        self.ponotb = p2
    def calcula_perimetro(self):
        a = self.pontob.x - self.pontoa.x
        b = self.pontob.y - self.pontoa.y
        perimetro = 2*a + 2*b
        return perimetro
    def calcula_area(self):
        a = self.pontob.x - self.pontoa.x
        b = self.pontob.y - self.pontoa.x
        area = a*b
        return area
        
        