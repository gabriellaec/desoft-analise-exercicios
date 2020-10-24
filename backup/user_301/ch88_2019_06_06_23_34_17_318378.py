class Retangulo:
    def _init__(self,P1,P2):
        self.P1x=P1.x
        self.P1y=P1.y
        self.P2x=P2.x
        self.P2y=P2.y
    
    def calcula_perimetro(self):
        ladox=self.P1x+self.P2x
        ladoy=self.P1y+self.pY
        perimetro=ladox+ladoy
        return perimetro
    	
    def calcula_area(self):
        area=self.P1x*P2y
        return area