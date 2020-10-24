class Retangulo:
    def __init__(self,Pie,Psd):
        Pie = self.p1
        Psd = self.p2
    def calcula_perimetro(self):
        a = Psd.y - Pie.y
        b = Psd.x - Pie.x
        return 2*(a+b)
    def calcula_area(self):
        a = Psd.y - Pie.y
        b = Psd.x - Pie.x
        return a*b