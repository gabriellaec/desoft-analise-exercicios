class Retangulo:
    def __init__(self, v1, v2):
        self.pie = v1
        self.psd = v2
    
    def calcula_perimetro(self):
        w = self.psd.x - self.pie.y
        z = self.psd.y - self.pie.x
        return 2 * (w+z)
    def calcula_area(self):
        w = self.psd.x - self.pie.y
        z = self.psd.y - self.pie.x
        return w*z
    
    

