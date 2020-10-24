class Retangulo:
    def __init__(self, pie, psd):
        self.pie = pie
        self.psd = psd
    def calcula_perimetro(self):
        a = self.psd.y - self.pie.y
        b = self.psd.x - self.pie.x        
        return 2*(a+b)
    def calcula_area(self):
        a = self.psd.y - self.pie.y
        b = self.psd.x - self.pie.x
        return a*b