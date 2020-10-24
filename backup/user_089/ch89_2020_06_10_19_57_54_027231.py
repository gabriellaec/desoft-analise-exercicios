class Circulo:
    def __init__(self,pc,r):
        self.pc.x = x
        self.pc.y = y
        self.r = float(r)
    
    def contem(self, ponto):
        self.ponto.y = y
        self.ponto.x = x
        d = ( (self.pc.x - self.ponto.x )**2 + ((self.pc.y - self.ponto.y)**2) ) ** (1/2)
        if d <= self.r:
            return True
        else: 
            return False
            