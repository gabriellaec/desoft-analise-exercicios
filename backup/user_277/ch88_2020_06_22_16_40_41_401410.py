def Retangulo(self, other_pointx_ #other_pointy):
    perimetro = 2 * (other_pointx - self.x) + 2 * (other_pointy - self.y)
    area = (other_pointx - self.x) * (other_pointy - self.y)
    return perimetro, area