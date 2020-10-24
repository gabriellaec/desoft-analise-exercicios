class Retangulo:
    def __init__(self,PIE,PSD):
        self.PIEx = PIE.x
        self.PIEy= PIE.y
        self.PSDx = PSD.x
        self.PSDy = PSD.y
    def calcula_perimetro(self):
        ladoX= (self.PSDx - self.PIEx)*2
        ladoY= (self.PSDy - self.PIEy)*2
        perimetro = ladoX + ladoY
        return perimentro
    def calcula_area(self):
        ladoX= (self.PSDx - self.PIEx)
        ladoY= (self.PSDy - self.PIEy)
        area= ladoX*ladoY
        return area
    