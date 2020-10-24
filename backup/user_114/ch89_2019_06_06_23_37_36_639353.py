class Circulo:
    def __init__(self,P,R):
        self.Px=P.x
        self.Py=P.y
        self.R=R
    def contem(self,ponto):
        if (self.Px**2+self.Py**2)<=self.R**2:
            return True
        else:
            return False
        