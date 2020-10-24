class Circulo:
    def __init__(self,ponto,raio):
        self.x=px
        self.y=py
        self.Raio=raio
        
    def contem(self,ponto):
        if(self.x-px)**2+(self.y-py)**2<=self.Raio**2:
            return True
        else:
            return False