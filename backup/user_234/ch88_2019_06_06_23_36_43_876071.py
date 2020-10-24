class Retangulo:
    def __init__(self, pie, psd):
        self.cie = pie
        self.csd = psd
    def calcula_perimetro(self):
        perimetro= 2*(self.csd.y-self.cie.y)+2*(self.csd.x-self.cie.x)
        return perimetro
    def calcula_area(self):
        area = (self.csd.y-self.cie.y)*(self.csd.x-self.cie.x)
        return area
            
            