class Retangulo:
    def __init__(self, p1, p2):
        self.i = p1
        self.s = p2
    def calcula_perimetro(self):
        comp = self.s.x - self.i.x
        alt = self.s.y - self.i.y
        return 2 * (alt + comp)
    def calcula_area(self):
        comp = self.s.x - self.i.x
        alt = self.s.y - self.i.y
        return comp * alt
    
# s = superior e i = inferior;