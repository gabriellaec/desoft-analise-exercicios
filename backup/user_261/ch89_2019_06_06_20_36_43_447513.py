class Circulo:
    def __init__(self,ponto,raio):
        self.x=ponto.x
        self.y=ponto.y
       	self.Raio=raio
    def contem(self,ponto):
        if ((ponto.x-self.x)**2+(ponto.y-self.y)**2)**0.5<=self.Raio:
            return True
        else:
            return False
        
    