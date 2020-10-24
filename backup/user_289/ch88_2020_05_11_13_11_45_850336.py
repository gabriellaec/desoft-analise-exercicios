class Retangulo:
    def calcula_perimetro(self):
        dy = self.y - self.x
        dx = self.x - self.y
        return 2*dx + 2*dy
    def calcula_area(self):
        dy = self.y - self.x
        dx = self.x - self.y
        return dx*dy