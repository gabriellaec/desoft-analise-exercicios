class Retangulo():
    def __init__(self,x,y,x2,y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
    def calcula_perimetro(self):
        lado_x = (self.x - self.x2)**2
        lado_y = (self.y-self.y2)**2
        p = lado_x+lado_y
        return p
    def calcula_area(self):
        area = (self.x - self.x2)*(self.y-self.y2)
        return area 
        