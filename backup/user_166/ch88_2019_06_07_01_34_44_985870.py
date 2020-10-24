class Retangulo:
    def __init__(self,PIE,PSD):
        self.PIEx = PIE.x
        self.PIEy= PIE.y
        self.PSDx = PSD.x
        self.PSDy = PSD.y
    def calcula_perimetro(self):
        ladoX= (self.PSD.x - self.PIE.x)*2
        ladoY= (self.PSD.y - self.PIE.y)*2
        perimetro = ladoX + ladoY
        return perimentro
    def calcula_area(self):
        ladoX= (self.PSD.x - self.PIE.x)
        ladoY= (self.PSD.y - self.PIE.y)
        area= ladoX*ladoY
        return area
    