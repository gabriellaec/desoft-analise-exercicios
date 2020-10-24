class Circulo:
    def __init__(self,ponto,raio):
        self.PontoX = ponto.x
        self.PontoY = ponto.y
        self.Raio = raio
        
    def contem(self,ponto):
        if (self.PontoX-ponto.x)**2+(self.PontoY-ponto.y)**2<=self.Raio**2:
            return True
        else:
            return False
           
            