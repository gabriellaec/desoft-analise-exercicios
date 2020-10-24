class Retangulo:
    def __init__(self,x1, x2, y1, y2):
        self.p1x = x1
        self.p2x = x2
        self.p1y = y1
        self.p2y = y2
    def calcula_perimetro(self):
        
        perim_x = (self.p2x - self.p1x) * 2
        if perim_x < 0:
            perim_x *= -1
            
        perim_y = (self.p2y - self.p1y) * 2
        if perim_y < 0:
            perim_y *= -1
            
        perim = perim_x + perim_y
        return perim
    def calcula_area(self):
        perim_x = (self.p2x - self.p1x) 
        if perim_x < 0:
            perim_x *= -1
            
        perim_y = (self.p2y - self.p1y)
        if perim_y < 0:
            perim_y *= -1
            
        area = (perim_x) * (perim_y)
        return area