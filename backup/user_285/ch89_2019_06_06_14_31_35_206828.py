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
        if ((self.Cx-self.x)**2 + (self.Cy-self.y)**2)>self.R**2:
            return False
        else:
            return True
        