class Retangulo:
    def __init__(self,ponto_ie,ponto_sd):
        self.a = ponto_ie
        self.b = ponto_sd
        
    def calcula_perimetro(self):
        perimetro = 2*(b.x - a.x)+2*(b.y-a.y)
        return perimetro
    def calcula_area(self):
        area = (b.x - a.x)*(b.y-a.y)
        return area