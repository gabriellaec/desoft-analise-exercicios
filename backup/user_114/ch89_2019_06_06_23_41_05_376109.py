class Circulo:
    def __init__(self,P,R):
        self.Px=P.x
        self.Py=P.y
        self.R=R
    def contem(self,P):
        if (self.Px-P.x)**2+(self.Py-P.y)**2<=self.R**2:
            return True
        else:
            return False
        