class Circulo:
    def __init__(self,ponto,raio):
        self.ponto = ponto
        self.raio = raio
        
    def contem(self,ponto2):
        x1 = self.ponto.x
        x2 = ponto2.x
        
        y1= self.ponto.y
        y2= ponto2.y
        d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        return (d <= self.raio)
        
        