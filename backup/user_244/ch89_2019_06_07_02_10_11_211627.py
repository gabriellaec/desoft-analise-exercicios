class Circulo():
    def __init__(self,P1,r):
        self.P1x = P1.x
        self.P1y = P1.y
        self.r = r
        
        
    def contem(self,P1):
        if (self.P1x-p1.x)**2+(self.P1x-P1.y)**2 <= self.r**2:
            return True
        else:
            return False
        