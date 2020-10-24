class Circulo:
    def __init__(self,ponto,float):
        self.x=ponto.x
        self.y=ponto.y
        self.radius=float
    def contem(self, ponto):
        if (self.x-ponto.x)**2+(self.y-ponto.y)**2<=self.radius**2:
            return True
        else:
            return False