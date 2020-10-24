class Circulo():
    def __init__(self, c, r):
        self.c=c
        self.r=r
    
    def contem(self, ponto):
        if ((self.ponto.x-self.c.x)**2+(self.ponto.y-self.c.y)**2)**0.5<=r:
            return True
        else:
            return False