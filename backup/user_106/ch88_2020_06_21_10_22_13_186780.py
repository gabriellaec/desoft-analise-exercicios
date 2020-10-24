class Retangulo:
    def __init__(self, pie, psd):
        self.pie = pie
        self.psd = psd
    def calcula_perimetro(self):
        a = psd.y - pie.y
        b = psd.x - pie.x        
        return 2*(a+b)
    def calcula_area(self):
        #a = psd.y - pie.y
        #b = psd.x - pie.x
        return a*b