class Circulo:
    def __init__(self,x,y,raio):
        self.centrox=x
        self.centroy=y
        self.raio=raio
    def contem (self,outroponto):
        dx=outroponto.x-self.centrox
        dy=outroponto.y-self.centroy
        d=((dx**2) + (dy**2)) ** 0.5
        if d>self.raio:
            return False
        else:
            return True