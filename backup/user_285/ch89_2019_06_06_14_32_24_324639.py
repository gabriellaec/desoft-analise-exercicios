class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Circulo:
    def __init__(self,C,R):
        self.Cx=C.x
        self.Cy=C.y
        self.R=R
        
    def contem(self,ponto):
        self.pontox=ponto.x
        self.pontoy=ponto.y
        if ((self.Cx-self.pontox)**2 + (self.Cy-self.pontoy)**2)>self.R**2:
            return False
        else:
            return True
        