class Retangulo:
    def __init__(self,Pie,Psd):
        Pie = self.Ponto(x, y)
        Psd = self.Ponto(x, y)
    def calcula_perimetro(self):
        a = Psd.y - Pie.y
        b = Psd.x - Pie.x
        return 2*(a+b)
    def calcula_area(self):
        a = Psd.y - Pie.y
        b = Psd.x - Pie.x
        return a*b