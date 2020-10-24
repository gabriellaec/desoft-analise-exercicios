class Retangulo:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        def calcura_perimetro(self):
            if self.x2 > self.x1:
            	perim_x = (self.x2 - self.x1) * 2
            else:
                perim_x = (self.x1 - self.x2) * 2
            if self.y2 > self.y1:
            	perim_y = (self.y2 - self.y1) * 2
            else:
                perim_y = (self.y1 - self.y2) * 2
            perim = perim_x + perim_y
            return perim
       	def calcula_area(self):
            if self.x2 > self.x1:
            	perim_x = (self.x2 - self.x1)
            else:
                perim_x = (self.x1 - self.x2)
            if self.y2 > self.y1:
            	perim_y = (self.y2 - self.y1)
            else:
                perim_y = (self.y1 - self.y2)
            area = (perim_x) * (perim_y)
            return area