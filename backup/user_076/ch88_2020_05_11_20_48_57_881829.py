class Retangulo:
    def __init__ (self,p1,p2):
        calcula_perimetro = 2*(abs(p1.x-p2.x)+abs(p1.y-p2.y))
        calcula_area = abs(p1.x - p2.x) * abs(p1.y - p2.y)