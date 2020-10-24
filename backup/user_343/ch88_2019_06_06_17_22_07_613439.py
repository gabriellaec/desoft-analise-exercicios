class Retangulo:
    def __init__(self,p1, p2):
        self.1x=p1.x
        self.2x=p2.x
        self.1y=p1.y
        self.2y=p2.y
        
    def calcula_perimetro(self):
        ladox=(self.2x-self.1x)
        ladoy=(self.2y-self.1y)
        perimetro=ladox*2+ladoy*2
        return perimetro
        
	
    def calcula_area(self):
        
        
        ladox=(self.2x-self.1x)
        ladoy=(self.2y-self.1y)
        area=ladox*ladoy
        return area
        