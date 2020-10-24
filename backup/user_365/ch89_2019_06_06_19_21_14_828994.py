class Circulo:
    def __init__(self,p,raio):
        self.x=p.x
        self.y=p.y
        self.Raio=raio
    def contem(self,ponto):
        if (self.x-ponto.x)**2+(self.y-ponto.y)**2<=self.Raio**2:
            return True
        else:
            return False