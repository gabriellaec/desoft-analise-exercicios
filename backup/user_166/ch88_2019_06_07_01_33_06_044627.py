class Retangulo:
    def __init__(self,PIE,PSD):
        self.PIEx = PIE.x
        self.PIEy= PIE.y
        self.PSDx = PSD.x
        self.PSDy = PSD.y
    def calcula_perimetro(self):
        ladoX= (PSD.x - PIE.x)*2
        ladoY= (PSD.y - PIE.y)*2
        perimetro = ladoX + ladoY
        return perimentro
    def calcula_area(self):
        ladoX= (PSD.x - PIE.x)
        ladoY= (PSD.y - PIE.y)
        area= ladoX*ladoY
        return area
    