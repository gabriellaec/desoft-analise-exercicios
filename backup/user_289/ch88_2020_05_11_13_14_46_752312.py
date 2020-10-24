class Retangulo:
    def calcula_perimetro(self, p1, p2):
        dy = p1.y - p2.y
        dx = p1.x - p2.y
        return 2*dx + 2*dy
    def calcula_area(self, p1, p2):
        dy = p1.y - p2.y
        dx = p1.x - p2.x
        return dx*dy