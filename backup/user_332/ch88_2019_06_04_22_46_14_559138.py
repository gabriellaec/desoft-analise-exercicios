class Retangulo:
    def __init__(self,p1.x, p2.x, p1.y, p2.y):
        self.p1x = p1.x
        self.p2x = p2.x
        self.p1y = p1.y
        self.p2y = p2.y
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