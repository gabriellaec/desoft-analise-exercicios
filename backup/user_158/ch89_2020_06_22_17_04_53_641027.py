from math import sqrt
class Circulo():
    def __init__(self,Ponto,R):
        self.R = R
        self.dentro = None
    
    def contem(self, ponto):
        D = sqrt((Ponto.x-ponto.x)**2) + ((Ponto.y-ponto.y)**2)
        if D <= R:
            self.dentro = True
        else: 
            self.dentro = False
        return self.dentro
    