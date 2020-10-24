from math import sqrt
class Circulo():
    def __init__(self,Ponto,R):
        self.R = R
        self.dentro = None
        self.centroX = Ponto.x
        self.centroY = Ponto.y
    
    def contem(self, ponto):
        D = sqrt((self.centroX-ponto.x)**2) + ((self.centroY-ponto.y)**2)
        if D <= self.R:
            self.dentro = True
        else: 
            self.dentro = False
        return self.dentro
    