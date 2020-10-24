class Retangulo():
    def __init__(self,x,y):
        self.P1x = x
        self.P1y = y
        self.P2x = x2
        self.P2y = y2
    def calcula_perimetro(self):
        lado_x = (x - x2)**2
        lado_y = (y-y2)**2
        p = lado_x+lado_y
        return p
    def calcula_area(self):
        area = (x - x2)*(y-y2)
        return area 
        