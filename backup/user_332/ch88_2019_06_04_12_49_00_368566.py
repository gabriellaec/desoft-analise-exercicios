class Retangulo:
   	def__init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        def calcura_perimetro(self):
            perim_x = (self.x2 - self.x1) * 2
            perim_y = (self.y2 - self.y1) * 2
            perim = perim_x + perim_y
            return perim
       	def calcula_area(self):
            area = (self.x2 - self.x1) * (self.y2 - self.y1)
            return area
            
        
    
    