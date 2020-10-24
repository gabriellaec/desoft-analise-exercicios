class Circulo:
    def __init__(self,P,R):
        self.centro=P
        self.raio=R
    def contem(self,ponto):
        C=False
        if ((self.centro.x-ponto.x)**2+(self.centro.y-ponto.y)**2)**0.5<=self.raio:
            C=True
        return C
 


        
        