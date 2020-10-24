class Retangulo():
    def __init__(self, l, h):
        self.lx = l*x
        self.hx = h*x
        self.ly = l*y
        self.hy = h*y
    def calcula_perimetro(self):
        ladoX = (self.hx - self.lx)*2
        ladoY=(self.hy - self.ly)*2
        perimetro = ladoX + ladoY
        return perimetro
    def calcula_area(self):
        ladoX = (self.hx - self.lx)
        ladoY = (self.hy - self.ly)
        return area