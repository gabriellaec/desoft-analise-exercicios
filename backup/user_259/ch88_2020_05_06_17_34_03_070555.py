class Retangulo:
    def __init__(self, p1, p2):
        self.pie = p1
        self.psd = p2
    
    def calcula_perimetro(self):
        a = self.psd.x - self.pie.x
        b = self.psd.y - self.pie.y
        return 2*(a+b)
    
    def calcula_area(self):
        a = self.psd.x - self.pie.x
        b = self.psd.y - self.pie.y
        return a*b
    