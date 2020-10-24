class Retangulo:
    def __init__(self, p1, p2):
        self.Iex = p1.x
        self.Iey = p1.y
        self.Sdx = p2.x
        self.Sdy = p2.y

    def calcula_perimetro(self):
        perimetro = 2 * (self.Iex - self.Sdx) + 2 * (self.Iey - self.Sdy)
        return perimetro

    def calcula_area(self):
        area = (self.Iex - self.Sdx) * (self.Iey - self.Sdy)
        return area
        