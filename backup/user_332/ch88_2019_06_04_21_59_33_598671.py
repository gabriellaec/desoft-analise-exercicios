class Retangulo:
    def __init__(self,p1.x, p2.x, p1.y, p2.y):
        self.p1x = p1.x
        self.p2x = p2.x
        self.p1y = p1.y
        self.p2y = p2.y
    def calcula_perimetro(self):
        if self.p1x < self.p2x:
            perim_x = (self.p2x - self.p1x) * 2
        else:
            perim_x = (self.p1x - self.p2x) * 2
        if self.p1y < self.p2y:
        	perim_y = (self.p2y - self.p1y) * 2
        else:
            perim_y = (self.p1y - self.p2y) * 2
        perim = perim_x + perim_y
        return perim
   	def calcula_area(self):
        if self.p2x > self.p1x:
        	perim_x = (self.p2x - self.p1x)
        else:
            perim_x = (self.p1x - self.p2x)
        if self.y2 > self.y1:
        	perim_y = (self.p2y - self.p1y)
        else:
            perim_y = (self.p1y - self.p2y)
        area = (perim_x) * (perim_y)
            return area