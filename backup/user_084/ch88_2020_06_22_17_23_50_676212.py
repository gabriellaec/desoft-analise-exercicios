from math import *
class retangulo:
    def __init__(self,P1,P2):
        self.IE=P1
        self.SD=P2
    def calcula_perimetro(self):
        P=2*(abs(self.IE.x-self.SD.x)+abs(self.IE.y+self.SD.y))
        return P
    def calcula_area(self):
        A=abs(self.IE.x-self.SD.x)*abs(self.IE.y-self.SD.y)
        return A