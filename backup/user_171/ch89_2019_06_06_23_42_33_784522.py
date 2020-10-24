class Circulo:
    def __init__(self,ponto,raio):
        self.x=p.x
        self.y=p.y
        self.Raio=raio
        
    def contem(self,ponto):
        if(self.x-p.x)**2+(self.y-p.y)**2<=self.Raio**2:
            return True
        else:
            return False