class Retangulo:
    def __init__(self,P1,P2):
        self.P1X=P1.x
        self.P2X=P2.x
        self.P1Y=P1.y
        self.P2Y=P2.y
        
    def calcula_perimetro(self):
        lado1=self.P2X - self.P1X
        lado2=self.P2Y - self.P1Y
        per=(lado1*2)+(lado2*2)
        return per
    
    def calcula_area(self):
        lado1=self.P2X - self.P1X
        lado2=self.P2Y - self.P1Y
        area=lado1*lado2
        return area