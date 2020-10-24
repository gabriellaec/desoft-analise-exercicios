class Retangulo:
    def __init__(self,x,y):
        self.y = y
        self.x = x
    def calcula_perimetro(self):
        self.perimetro = self.x + self.x + self.y + self.y
    def calcula_area (self):
        self.area = self.x * self.y
        