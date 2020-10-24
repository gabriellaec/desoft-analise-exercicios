class Retangulo:
    def __init__(self, PIE, PSD):
        self.PIEx = PIE.x
        self.PSDx = PSD.x
        self.PIEy = PIE.y
        self.PSDy = PSD.y
    
    def calcula_perimetro(self):
        ladosx = (self.PSDx - self.PIEx)*2
        ladosy = (self.PSDy - self.PIEy)*2
        perimetro = ladosx + ladosy
        return perimetro
    
    def calcula_area(self):
        ladosx = (self.PSDx - self.PIEx)
        ladosy = (self.PSDy - self.PIEy)
        area = ladosx*ladosy
        return area