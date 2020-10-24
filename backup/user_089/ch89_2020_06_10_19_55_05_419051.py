class Circulo:
    def __init__(self,c,r):
        self.c.x = c.x
        self.c.y = c.y
        self.r = float(r)
    
    def contem(self, ponto):
        d = ( (self.c.x-self.ponto.x )**2 + ((self.c.y-self.ponto.y)**2) ) ** (1/2)
        if d <= self.r:
            return True
        else: 
            return False
            