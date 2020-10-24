class Retangulo:
    def __init__(self,x,y):
        self.p1x=p1.x
        self.p1y=p1.y
        self.p2x=p2.x
        self.p2y=p2.y
     
    ladox=(self.p2x - self.p1x)
    ladoy=(self.p2y - self.p1y)
   	def calcula_perimetro(self):
        perimetro=ladox*2 + ladoy*2
   		return perimetro
    def calcula_area(self):
        area=ladox*ladoy
        return area

	
