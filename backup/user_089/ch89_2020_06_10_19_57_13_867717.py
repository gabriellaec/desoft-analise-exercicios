class Circulo:
    def __init__(self,pc,r):
        self.pc.x = pc.x
        self.pc.y = pc.y
        self.r = float(r)
    
    def contem(self, ponto):
        self.ponto.y = ponto.y
        self.ponto.x = ponto.x
        d = ( (self.pc.x - self.ponto.x )**2 + ((self.pc.y - self.ponto.y)**2) ) ** (1/2)
        if d <= self.r:
            return True
        else: 
            return False
            