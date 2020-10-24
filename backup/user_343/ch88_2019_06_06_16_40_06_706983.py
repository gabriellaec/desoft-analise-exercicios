class Retangulo:
    def __init__(self,p1, p2):
        self.p1x=p1.x
        self.p2x=p2.x
        self.p1y=p1.y
        self.p2y=p2.y
        
    def calcula_perimetro(self):
        ladox=(self.p2x-self.p1x)
        ladoy=(self.p2y-self.p1y)
        perimetro=ladox*2+ladoy*2
        return perimetro
        
   	def calcula_area(self):
        ladox=(self.p2x-self.p1x)
        ladoy=(self.p2y-self.p1y)
        area=ladox*ladoy
        return area
        