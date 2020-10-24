class Retangulo:
    def __init__(self, pie, psd):
        self.pie = pie
        self.psd = psd
    def calcula_perimetro(self):
        perimetro= 2*(self.psd.y-self.pie.y)+2*(self.psd.x-self.pie.x)
        return perimetro
    def calcula_area(self):
        area = (self.psd.y-self.pie.y)*(self.psd.x-self.pie.x)
        return area
            
            