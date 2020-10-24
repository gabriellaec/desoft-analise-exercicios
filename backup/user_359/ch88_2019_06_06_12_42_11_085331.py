class Retangulo:
    def__init__(self, x, y):
        self.bottomleft = x
        self.topright = y
	def calcula_perimetro(self):
        perimetro = self.bottomleft + self.topright self.bottomleft + self.topright
        return perimetro
    def calcula_area(self):
        area = self.bottomleft * self.topright
        return area