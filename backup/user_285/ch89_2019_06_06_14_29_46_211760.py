class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Circulo:
    def __init__(self,C,R,ponto):
        self.Cx=C.x
        self.Cy=C.y
        self.R=R
        self.pontox=ponto.x
        self.pontoy=ponto.y
        
    def contem(self,ponto):
        if ((self.Cx-self.pontox)**2 + (self.Cy-self.pontoy)**2)>R**2:
            return False
        else:
            return True
        