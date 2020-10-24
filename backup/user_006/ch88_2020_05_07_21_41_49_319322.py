class Retangulo:
    def __init__(self, p1, p2):
        self.ie= p1
        self.sd= p2
    def calcula_perimetro(self):
        a = self.sd.x -self.ie.x
        b = self.sd.y - self.ie.y
        per= 2*a+2*b
        return per
    def calcula_area(self):
        a = self.sd.x -self.ie.x
        b = self.sd.y - self.ie.y
        area=a*b
        return area