class Retangulo:
    def __init__(self,P1,P2):
        self.P1x=P1.x
        self.P1y=P1.y
        self.P2x=P2.x
        self.P2y=P2.y
        self.lado1=self.P2x-self.P1x
        self.lado2=self.P2y-self.P1y
    def calcula_perimetro(self):
        return 2*self.lado1+2*self.lado2
    
    def calcula_area(self): 
        return self.lado1*self.lado2