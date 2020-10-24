class Circulo:
    def __init__(self,ponto):
        self.center.x=ponto.x
        self.center.y=ponto.y
        self.radius=float
    def contem(self, ponto):
        if (self.center.x-ponto.x)**2+(self.center.y-ponto.y)**2<=self.radius**2:
            return True
        else:
            return False