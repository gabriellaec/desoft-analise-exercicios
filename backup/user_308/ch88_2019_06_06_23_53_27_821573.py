class Retangulo:
    def __init__(self,P1,P2):
        P1X=P1.x
        P1Y=P1.y
        P2X=P2.x
        P2Y=P2.y

    def calcula_perimetro(self):
        lado1=self.P2X - self.P1X
        lado2=self.P2Y - self.P2X
		per=(lado1*2)+(lado2*2)
		return per
    
	def calcula_area(self):
        lado1=self.P2X - self.P1X
        lado2=self.P2Y - self.P2X
        area=lado1*lado2
        return area
        
        