class Pontos:
    def __init__(self,x,y):
        self.x= x
        self.y=y
class Retangulo(self,P1,P2):
    self.P1x= P1.x
    self.P1y=P1.y
    self.P2x= P2.x
    self.P2y= P2.y
  
    def calcula_perimetro(self):
        ladoX= (self.P1x-self.P2x)
        ladoY= (self.P1y-self.P2y)
        perimetro= 2*(ladoX)+ 2*(ladoY)
        return perimetro
    def calcula_area(self):
        ladoX= (self.P1x-self.P2x)
        ladoY= (self.P1y-self.P2y)
        area=ladoX*ladoY
        return area