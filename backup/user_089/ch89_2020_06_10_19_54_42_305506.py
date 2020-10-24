class Circulo:
    def __init__(self,circ,r):
        self.c.x = circ.x
        self.c.y = circ.y
        self.r = float(r)
    
    def contem(self, ponto):
        d = ( (self.c.x-self.ponto.x )**2 + ((self.c.y-self.ponto.y)**2) ) ** (1/2)
        if d <= self.r:
            return True
        else: 
            return False
            