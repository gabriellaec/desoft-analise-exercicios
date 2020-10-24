class Retangulo(self, ie, sd):
    def __init__(ie, sd):
        self.x1 = ie.x
        self.x2 = sd.x
        self.y1 = ie.y
        self.y2 = sd.y
        self.xt = self.x2 - self.x1
        self.yt = self.y2 - self.y1
    def calcula_perimetro(self):
        self.perimetro = self.xt*2 + self.yt*2
    def calcula_area(self):
        self.area = self.xt * self.yt