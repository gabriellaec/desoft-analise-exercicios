class Retangulo:
    def __init__(self, other_point):
        perimetro_x = 2 * (other_point.x - self.x)
        perimetro_y = 2 * (other_point.y - self.y)
        perimetro = perimetro_y + perimetro_x
        return perimetro
    
    def __init__(self, other_point):
        base = other_point.x - self.x
        altura = other_point.y - self.y
        area = base * altura
        return area